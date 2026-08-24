/* Exact level DP for the canonical-pattern value.
   State = packed per-epsilon used-variable masks (9 bits x 6 = 54 bits, u64).
   In static copy order the depositor-parity term vanishes and future subtree
   values depend only on (depth, masks) => forward DP is exact.
   cur level: streamed from disk file (iterated only).
   nxt level: open-addressing hash in RAM; spills sorted runs to disk when full;
   runs merged (weights summed, zeros dropped) into the next level file.
   Modes: quad | quad0 | quadq | det3 [maxlevel] | det3sub c
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>
#include <sys/statvfs.h>
#include <unistd.h>

static int NF, NE, NLEG, NV = 9;
static int NOPT[24];
static int OE[24][1024][3], OV[24][1024][3]; static long long OS[24][1024];
static int OL[24][1024];
static int FIXROOT = -1; static long long FMULT = 1;
static int EW[8], EOFF[8];   /* per-antisymmetrizer field width and bit offset */
static int NGRP; static uint64_t GMASK[8]; static int GTOT[8];
static int GMINSUF[8][25], GMAXSUF[8][25];  /* suffix min/max group contribution from copies >= lv */
static time_t t0;
static void default_widths(void) {
    for (int e = 0; e < NE; e++) EW[e] = 9;
    int off = 0;
    for (int e = 0; e < NE; e++) { EOFF[e] = off; off += EW[e]; }
}

/* ---------- pattern setups (identical tables to bit3.c) ---------- */
static int TRI[24][3];
static int fact_i(int n){int r=1;for(int i=2;i<=n;i++)r*=i;return r;}
/* distinct ordered arrangements of the NLEG-multiset vs[]; returns count, fills arr */
static int arrangements(int *vs, int nleg, int arr[][3]) {
    int idx[3] = {0,1,2}, n = 0;
    /* enumerate all nleg! index-permutations, dedup resulting tuples */
    int perms2[2][2] = {{0,1},{1,0}};
    int perms3[6][3] = {{0,1,2},{0,2,1},{1,0,2},{1,2,0},{2,0,1},{2,1,0}};
    int np = nleg == 3 ? 6 : 2;
    for (int p = 0; p < np; p++) {
        int cand[3];
        for (int k = 0; k < nleg; k++)
            cand[k] = vs[nleg == 3 ? perms3[p][k] : perms2[p][k]];
        int dup = 0;
        for (int q = 0; q < n && !dup; q++) {
            int same = 1;
            for (int k = 0; k < nleg; k++) if (arr[q][k] != cand[k]) same = 0;
            if (same) dup = 1;
        }
        if (!dup) { for (int k = 0; k < nleg; k++) arr[n][k] = cand[k]; n++; }
    }
    (void)idx;
    return n;
}
static void setup_evalfile(const char *path, int withwidths) {
    FILE *f = fopen(path, "r");
    if (!f) { fprintf(stderr, "cannot open %s\n", path); exit(1); }
    if (fscanf(f, "%d %d %d %d", &NV, &NE, &NF, &NLEG) != 4) { fprintf(stderr, "bad header\n"); exit(1); }
    if (NE > 8 || NF > 24) { fprintf(stderr, "dims too big\n"); exit(1); }
    if (withwidths) {
        int off = 0;
        for (int e = 0; e < NE; e++) {
            if (fscanf(f, "%d", &EW[e]) != 1) { fprintf(stderr, "bad widths\n"); exit(1); }
            EOFF[e] = off; off += EW[e];
        }
        if (off > 60) { fprintf(stderr, "state too wide\n"); exit(1); }
    } else default_widths();
    for (int i = 0; i < NF; i++)
        for (int k = 0; k < NLEG; k++)
            if (fscanf(f, "%d", &TRI[i][k]) != 1) { fprintf(stderr, "bad TRI\n"); exit(1); }
    int nmon;
    if (fscanf(f, "%d", &nmon) != 1) { fprintf(stderr, "bad nmon\n"); exit(1); }
    static long long mc[256]; static int mv[256][3];
    for (int m = 0; m < nmon; m++) {
        if (fscanf(f, "%lld", &mc[m]) != 1) { fprintf(stderr, "bad coeff\n"); exit(1); }
        for (int k = 0; k < NLEG; k++)
            if (fscanf(f, "%d", &mv[m][k]) != 1) { fprintf(stderr, "bad var\n"); exit(1); }
    }
    if (fscanf(f, "%d %lld", &FIXROOT, &FMULT) != 2) { FIXROOT = -1; FMULT = 1; }
    fclose(f);
    int fl = fact_i(NLEG);
    for (int i = 0; i < NF; i++) {
        int n = 0;
        for (int m = 0; m < nmon; m++) {
            int arr[6][3];
            int na = arrangements(mv[m], NLEG, arr);
            long long w = mc[m] * (fl / na);
            for (int a = 0; a < na; a++) {
                int okw = 1;
                for (int k = 0; k < NLEG; k++)
                    if (arr[a][k] >= EW[TRI[i][k]]) { okw = 0; break; }   /* short-column filter */
                if (!okw) continue;
                if (n >= 1024) { fprintf(stderr, "too many options\n"); exit(1); }
                for (int k = 0; k < NLEG; k++) { OE[i][n][k] = TRI[i][k]; OV[i][n][k] = arr[a][k]; }
                OS[i][n] = w; OL[i][n] = NLEG; n++;
            }
        }
        NOPT[i] = n;
    }
}

static void setup_evalopts(const char *path) {
    FILE *f = fopen(path, "r");
    if (!f) { fprintf(stderr, "cannot open %s\n", path); exit(1); }
    if (fscanf(f, "%d %d", &NE, &NF) != 2) { fprintf(stderr, "bad header\n"); exit(1); }
    int off = 0;
    for (int e = 0; e < NE; e++) {
        if (fscanf(f, "%d", &EW[e]) != 1) { fprintf(stderr, "bad widths\n"); exit(1); }
        EOFF[e] = off; off += EW[e];
    }
    if (off > 60 || NF > 24) { fprintf(stderr, "too wide\n"); exit(1); }
    if (fscanf(f, "%d", &NGRP) != 1) { fprintf(stderr, "bad ngrp\n"); exit(1); }
    for (int g = 0; g < NGRP; g++) {
        int nv2;
        if (fscanf(f, "%d %d", &GTOT[g], &nv2) != 2) { fprintf(stderr, "bad grp\n"); exit(1); }
        GMASK[g] = 0;
        for (int q = 0; q < nv2; q++) { int v; fscanf(f, "%d", &v); GMASK[g] |= 1ULL << v; }
    }
    for (int i = 0; i < NF; i++) {
        int no;
        if (fscanf(f, "%d", &no) != 1 || no > 1024) { fprintf(stderr, "bad nopt\n"); exit(1); }
        NOPT[i] = no;
        for (int o = 0; o < no; o++) {
            long long w; int L;
            if (fscanf(f, "%lld %d", &w, &L) != 2 || L > 3) { fprintf(stderr, "bad opt\n"); exit(1); }
            OS[i][o] = w; OL[i][o] = L;
            for (int k = 0; k < L; k++) {
                if (fscanf(f, "%d %d", &OE[i][o][k], &OV[i][o][k]) != 2) { fprintf(stderr, "bad leg\n"); exit(1); }
                if (OV[i][o][k] >= EW[OE[i][o][k]]) { fprintf(stderr, "leg exceeds width\n"); exit(1); }
            }
        }
    }
    if (fscanf(f, "%lld", &FMULT) != 1) FMULT = 1;
    fclose(f);
    /* suffix min/max group contributions */
    for (int g = 0; g < NGRP; g++) {
        GMINSUF[g][NF] = GMAXSUF[g][NF] = 0;
        for (int i = NF-1; i >= 0; i--) {
            int mn = 99, mx = -1;
            for (int o = 0; o < NOPT[i]; o++) {
                int cgrp = 0;
                for (int k = 0; k < OL[i][o]; k++)
                    if (GMASK[g] >> OV[i][o][k] & 1) cgrp++;
                if (cgrp < mn) mn = cgrp;
                if (cgrp > mx) mx = cgrp;
            }
            if (mx < 0) { mn = 0; mx = 0; }
            GMINSUF[g][i] = GMINSUF[g][i+1] + mn;
            GMAXSUF[g][i] = GMAXSUF[g][i+1] + mx;
        }
    }
}
static void setup_det3(int isperm) {
    NF = 18; NE = 6; NLEG = 3;
    default_widths();
    int raw[20][3]; int nraw = 0, idx = 0;
    for (int a = 0; a < 6; a++) for (int b = a+1; b < 6; b++) for (int c = b+1; c < 6; c++) {
        if (a==0&&b==1&&c==2) continue; if (a==3&&b==4&&c==5) continue;
        raw[nraw][0]=a; raw[nraw][1]=b; raw[nraw][2]=c; nraw++;
    }
    for (int pass = 0; pass < 3; pass++)
        for (int r = 0; r < nraw; r++) {
            int has[3] = {0,0,0};
            for (int k = 0; k < 3; k++) for (int q = 0; q < 3; q++) if (raw[r][k] == q) has[q] = 1;
            int cls = has[0] ? 0 : (has[1] ? 1 : 2);
            if (cls == pass) { TRI[idx][0]=raw[r][0]; TRI[idx][1]=raw[r][1]; TRI[idx][2]=raw[r][2]; idx++; }
        }
    static const int DM[6][3] = { {0,4,8},{0,5,7},{1,3,8},{1,5,6},{2,3,7},{2,4,6} };
    static const int DS[6]     = { 1, -1, -1, 1, 1, -1 };
    static const int P[6][3] = {{0,1,2},{0,2,1},{1,0,2},{1,2,0},{2,0,1},{2,1,0}};
    for (int i = 0; i < NF; i++) {
        int n = 0;
        for (int m = 0; m < 6; m++) for (int p = 0; p < 6; p++) {
            for (int k = 0; k < 3; k++) { OE[i][n][k] = TRI[i][k]; OV[i][n][k] = DM[m][P[p][k]]; }
            OS[i][n] = isperm ? 1 : DS[m]; OL[i][n] = 3; n++;
        }
        NOPT[i] = n;
    }
}
static void setup_quad(int degenerate) {
    NF = 4; NE = 2; NLEG = 2;
    default_widths();
    for (int i = 0; i < NF; i++) {
        int n = 0;
        if (!degenerate) {
            int mons[2][2] = {{0,3},{1,2}}; int ms[2] = {1, -1};
            for (int m = 0; m < 2; m++) for (int p = 0; p < 2; p++) {
                OE[i][n][0] = 0; OE[i][n][1] = 1;
                OV[i][n][0] = mons[m][p]; OV[i][n][1] = mons[m][1-p];
                OS[i][n] = ms[m]; OL[i][n] = 2; n++;
            }
        } else {
            int mons[1][2] = {{0,3}};
            for (int p = 0; p < 2; p++) {
                OE[i][n][0] = 0; OE[i][n][1] = 1;
                OV[i][n][0] = mons[0][p]; OV[i][n][1] = mons[0][1-p];
                OS[i][n] = 1; OL[i][n] = 2; n++;
            }
        }
        NOPT[i] = n;
    }
}

/* ---------- hash table with spill runs ---------- */
#define LOGCAP 26
#define CAPQ ((size_t)1 << LOGCAP)
#define MAXLOAD ((size_t)(CAPQ * 55 / 100))
static uint64_t *hkey; static int64_t *hval; static size_t hcount;
#define MAXRUNS 64
static int nruns; static char runname[MAXRUNS][64];
static long long emitted;

static inline uint64_t mix(uint64_t x) {
    x ^= x >> 33; x *= 0xff51afd7ed558ccdULL;
    x ^= x >> 33; x *= 0xc4ceb9fe1a85ec53ULL;
    x ^= x >> 33; return x;
}
typedef struct { uint64_t k; int64_t v; } Rec;
static int reccmp(const void *a, const void *b) {
    uint64_t ka = ((const Rec*)a)->k, kb = ((const Rec*)b)->k;
    return ka < kb ? -1 : (ka > kb ? 1 : 0);
}

/* ---------- delta-varint codec for sorted (key,value) streams ---------- */
typedef struct { FILE *f; uint64_t prev; long long recs, bytes; } CW;
typedef struct { FILE *f; uint64_t prev; int eof; } CR;
static void cw_open(CW *w, const char *name, const char *mode, uint64_t prev, long long bytes) {
    w->f = fopen(name, mode);
    if (!w->f) { fprintf(stderr, "CW OPEN %s FAILED\n", name); exit(3); }
    setvbuf(w->f, NULL, _IOFBF, 1 << 22);
    w->prev = prev; w->recs = 0; w->bytes = bytes;
}
static inline void cw_varint(CW *w, uint64_t x) {
    while (x >= 128) { putc_unlocked((int)(x & 127) | 128, w->f); x >>= 7; w->bytes++; }
    putc_unlocked((int)x, w->f); w->bytes++;
}
static inline void cw_rec(CW *w, uint64_t k, int64_t v) {
    cw_varint(w, k - w->prev);
    uint64_t zz = ((uint64_t)v << 1) ^ (uint64_t)(v >> 63);
    cw_varint(w, zz);
    w->prev = k; w->recs++;
}
static void cw_close(CW *w) {
    if (fflush(w->f) != 0 || ferror(w->f) || fclose(w->f) != 0) { fprintf(stderr, "CW CLOSE FAILED\n"); exit(3); }
    w->f = NULL;
}
static void cr_open(CR *r, const char *name, long long byteoff, uint64_t prev) {
    r->f = fopen(name, "rb");
    if (!r->f) { fprintf(stderr, "CR OPEN %s FAILED\n", name); exit(3); }
    setvbuf(r->f, NULL, _IOFBF, 1 << 20);
    if (byteoff) fseek(r->f, byteoff, SEEK_SET);
    r->prev = prev; r->eof = 0;
}
static inline int cr_varint(CR *r, uint64_t *x) {
    uint64_t v = 0; int sh = 0, c;
    if ((c = getc_unlocked(r->f)) == EOF) return 0;
    for (;;) {
        v |= (uint64_t)(c & 127) << sh;
        if (!(c & 128)) break;
        sh += 7;
        if ((c = getc_unlocked(r->f)) == EOF) { fprintf(stderr, "TRUNCATED STREAM\n"); exit(3); }
    }
    *x = v; return 1;
}
static inline int cr_rec(CR *r, uint64_t *k, int64_t *v) {
    uint64_t d, zz;
    if (!cr_varint(r, &d)) { r->eof = 1; return 0; }
    if (!cr_varint(r, &zz)) { fprintf(stderr, "TRUNCATED STREAM\n"); exit(3); }
    r->prev += d;
    *k = r->prev;
    *v = (int64_t)(zz >> 1) ^ -(int64_t)(zz & 1);
    return 1;
}
static void cr_close(CR *r) { if (r->f) fclose(r->f); r->f = NULL; }

static double BUDGET = 6.0e9;
static long long levbytes;
static int KB;
#define BUCK 10
static inline int shard_of(uint64_t key, int P) {
    return (int)((((key >> (KB - BUCK)) & ((1u << BUCK) - 1)) * (uint64_t)P) >> BUCK);
}
static void diskwait2(double need) {
    for (;;) {
        struct statvfs sv;
        if (statvfs(".", &sv) != 0) return;
        double freeb = (double)sv.f_bavail * sv.f_frsize;
        if (freeb > need) return;
        fprintf(stderr, "  low disk (%.1f GB) - waiting\n", freeb/1e9);
        sleep(60);
    }
}
static void spill(void) {
    if (nruns >= MAXRUNS) { fprintf(stderr, "RUN OVERFLOW\n"); exit(4); }
    Rec *arr = malloc(hcount * sizeof(Rec) + 1);
    if (!arr) { fprintf(stderr, "SPILL ALLOC FAILED\n"); exit(4); }
    size_t n = 0;
    for (size_t i = 0; i < CAPQ; i++)
        if (hkey[i]) { arr[n].k = hkey[i]; arr[n].v = hval[i]; n++; }
    qsort(arr, n, sizeof(Rec), reccmp);
    sprintf(runname[nruns], "run_%d.dat", nruns);
    diskwait2(2.0e9);
    CW w; cw_open(&w, runname[nruns], "wb", 0, 0);
    for (size_t i = 0; i < n; i++) cw_rec(&w, arr[i].k, arr[i].v);
    cw_close(&w);
    free(arr);
    levbytes += w.bytes;
    fprintf(stderr, "  spill run %d: %zu recs %lld MB (t %.0f)\n", nruns, n, w.bytes >> 20, difftime(time(NULL), t0));
    nruns++;
    memset(hkey, 0, CAPQ * sizeof(uint64_t));
    hcount = 0;
}
static inline void hinsert(uint64_t key, int64_t v) {
    /* pure insert: drivers spill at record boundaries (checkpoint safety) */
    size_t i = mix(key) & (CAPQ - 1);
    for (;;) {
        if (hkey[i] == key) { hval[i] += v; return; }
        if (!hkey[i]) {
            if (hcount >= CAPQ - 2048) { fprintf(stderr, "TABLE OVERFULL\n"); exit(4); }
            hkey[i] = key; hval[i] = v; hcount++; return;
        }
        i = (i + 1) & (CAPQ - 1);
    }
}

/* merge spill runs + table into level file; return state count */
/* merge current runs, APPEND to writer w (codec state persists) */
static long long merge_append(CW *w, long long *sumabs) {
    CR rd[MAXRUNS]; uint64_t ks[MAXRUNS]; int64_t vs[MAXRUNS]; int alive[MAXRUNS];
    double runbytes = 0;
    for (int i = 0; i < nruns; i++) {
        FILE *tf = fopen(runname[i], "rb");
        if (tf) { fseek(tf, 0, SEEK_END); runbytes += (double)ftell(tf); fclose(tf); }
    }
    diskwait2(runbytes * 0.6 + 1.0e9);
    for (int i = 0; i < nruns; i++) {
        cr_open(&rd[i], runname[i], 0, 0);
        alive[i] = cr_rec(&rd[i], &ks[i], &vs[i]);
    }
    long long states = 0; *sumabs = 0;
    for (;;) {
        int best = -1;
        for (int i = 0; i < nruns; i++)
            if (alive[i] && (best < 0 || ks[i] < ks[best])) best = i;
        if (best < 0) break;
        uint64_t k = ks[best]; int64_t v = 0;
        for (int i = 0; i < nruns; i++)
            while (alive[i] && ks[i] == k) { v += vs[i]; alive[i] = cr_rec(&rd[i], &ks[i], &vs[i]); }
        if (v) { cw_rec(w, k, v); states++; *sumabs += v > 0 ? v : -v; }
    }
    for (int i = 0; i < nruns; i++) cr_close(&rd[i]);
    return states;
}
/* legacy whole-level merge into a fresh file (non-checkpointed modes) */
static long long merge_out(const char *outname, long long *sumabs, int delruns) {
    CW w; cw_open(&w, outname, "wb", 0, 0);
    long long states = merge_append(&w, sumabs);
    cw_close(&w);
    for (int i = 0; i < nruns; i++) if (delruns) remove(runname[i]);
    if (delruns) nruns = 0;
    return states;
}

/* ---------- transition ---------- */
static int FILT_P = 1, FILT_SHARD = 0;
static inline void process_rec(uint64_t key, int64_t w, int copy) {
    int pg[8];
    int nopt = NOPT[copy];
    for (int g = 0; g < NGRP; g++) {
        int cnt = 0;
        for (int e = 0; e < NE; e++)
            cnt += __builtin_popcountll((key >> EOFF[e]) & ((1u << EW[e]) - 1) & GMASK[g]);
        pg[g] = cnt;
    }
    for (int o = 0; o < nopt; o++) {
        uint64_t nk = key; int64_t s = w * OS[copy][o];
        int ok = 1;
        for (int k2 = 0; k2 < OL[copy][o]; k2++) {
            int e = OE[copy][o][k2], v = OV[copy][o][k2];
            uint64_t m = (nk >> EOFF[e]) & ((1u << EW[e]) - 1);
            if (m >> v & 1) { ok = 0; break; }
            if (__builtin_popcountll(m >> (v+1)) & 1) s = -s;
            nk |= 1ULL << (EOFF[e] + v);
        }
        if (!ok) continue;
        if (NGRP) {
            for (int g = 0; g < NGRP; g++) {
                int cnt = pg[g];
                for (int k2 = 0; k2 < OL[copy][o]; k2++)
                    if (GMASK[g] >> OV[copy][o][k2] & 1) cnt++;
                if (cnt + GMAXSUF[g][copy+1] < GTOT[g] || cnt + GMINSUF[g][copy+1] > GTOT[g]) { ok = 0; break; }
            }
            if (!ok) continue;
        }
        if (FILT_P <= 1 || shard_of(nk, FILT_P) == FILT_SHARD) { hinsert(nk, s); emitted++; }
    }
}
static long long do_level(const char *inname, const char *outname, int copy) {
    CR in; cr_open(&in, inname, 0, 0);
    uint64_t k; int64_t v;
    emitted = 0; levbytes = 0;
    while (cr_rec(&in, &k, &v)) {
        if (hcount >= MAXLOAD) spill();
        process_rec(k, v, copy);
    }
    cr_close(&in);
    if (hcount || nruns == 0) spill();
    long long sumabs;
    long long states = merge_out(outname, &sumabs, 1);
    fprintf(stderr, "level %d: states %lld emitted %lld sum|w| %lld (t %.0f)\n",
            copy + 1, states, emitted, sumabs, difftime(time(NULL), t0));
    return states;
}

/* ---------- resumable sharded driver (evalopts grind mode) ---------- */
static char CKIN[256];
typedef struct {
    int lev, P, shard, phase, nruns;
    long long inrec, inbyte;
    uint64_t inprev;
    long long outrec, outbyte; uint64_t outprev;
    long long st_acc, sum_acc, em_acc, by_acc;
} CK;
static void ckwrite2(const CK *c) {
    FILE *f = fopen("ck.tmp", "w");
    if (!f) { fprintf(stderr, "CK OPEN FAILED\n"); exit(3); }
    if (fprintf(f, "ck2 %s %d %d %d %d %lld %lld %llu %d %lld %lld %llu %lld %lld %lld %lld\n",
        CKIN, c->lev, c->P, c->shard, c->phase, c->inrec, c->inbyte,
        (unsigned long long)c->inprev, c->nruns, c->outrec, c->outbyte,
        (unsigned long long)c->outprev, c->st_acc, c->sum_acc, c->em_acc, c->by_acc) < 0)
        { fprintf(stderr, "CK WRITE FAILED\n"); exit(3); }
    if (fclose(f) != 0 || rename("ck.tmp", "ck.txt") != 0) { fprintf(stderr, "CK RENAME FAILED\n"); exit(3); }
}
static int ckread2(CK *c) {
    FILE *f = fopen("ck.txt", "r");
    if (!f) return 0;
    char tag[8], nm[256]; unsigned long long ip, op;
    int ok = fscanf(f, "%7s %255s %d %d %d %d %lld %lld %llu %d %lld %lld %llu %lld %lld %lld %lld",
        tag, nm, &c->lev, &c->P, &c->shard, &c->phase, &c->inrec, &c->inbyte, &ip,
        &c->nruns, &c->outrec, &c->outbyte, &op, &c->st_acc, &c->sum_acc, &c->em_acc, &c->by_acc) == 17;
    fclose(f);
    c->inprev = ip; c->outprev = op;
    return ok && !strcmp(tag, "ck2") && !strcmp(nm, CKIN);
}
static void rmglob(void) {
    char nm[64];
    for (int i = 0; i < MAXRUNS; i++) { sprintf(nm, "run_%d.dat", i); remove(nm); }
    remove("levtmp.dat"); remove("ck.tmp");
}
static void do_level_ck2(CK *c) {
    char inname[64], outname[64];
    sprintf(inname, "lev%d.dat", c->lev);
    sprintf(outname, "lev%d.dat", c->lev + 1);
restart_level:
    FILT_P = c->P;
    for (; c->shard < c->P; ) {
        FILT_SHARD = c->shard;
        if (c->phase == 0) {
            nruns = c->nruns;
            for (int i = 0; i < nruns; i++) sprintf(runname[i], "run_%d.dat", i);
            levbytes = 0;
            for (int i = 0; i < nruns; i++) {
                FILE *tf = fopen(runname[i], "rb");
                if (tf) { fseek(tf, 0, SEEK_END); levbytes += ftell(tf); fclose(tf); }
            }
            memset(hkey, 0, CAPQ * sizeof(uint64_t));
            hcount = 0;
            emitted = 0;
            CR in; cr_open(&in, inname, c->inbyte, c->inprev);
            uint64_t k; int64_t v;
            long long inrec = c->inrec;
            int aborted = 0;
            for (;;) {
                if (hcount >= MAXLOAD) {
                    /* record boundary: everything decoded so far is processed */
                    spill();
                    c->inrec = inrec;
                    c->inbyte = ftell(in.f);   /* exact: stdio tracks logical pos */
                    c->inprev = in.prev;
                    c->nruns = nruns;
                    c->em_acc += emitted; emitted = 0;
                    ckwrite2(c);
                    if (levbytes > BUDGET && c->P < 64) { aborted = 1; break; }
                }
                if (!cr_rec(&in, &k, &v)) break;
                process_rec(k, v, c->lev);
                inrec++;
            }
            cr_close(&in);
            if (aborted) {
                for (int i = 0; i < nruns; i++) remove(runname[i]);
                nruns = 0;
                c->P *= 2; c->shard = 0; c->phase = 0;
                c->inrec = 0; c->inbyte = 0; c->inprev = 0; c->nruns = 0;
                c->outrec = 0; c->outbyte = 0; c->outprev = 0;
                c->st_acc = 0; c->sum_acc = 0; c->em_acc = 0; c->by_acc = 0;
                truncate("levtmp.dat", 0);
                ckwrite2(c);
                fprintf(stderr, "  budget hit: resharding level %d with P=%d (t %.0f)\n",
                        c->lev + 1, c->P, difftime(time(NULL), t0));
                goto restart_level;
            }
            if (hcount) spill();
            c->em_acc += emitted; emitted = 0;
            c->phase = 1; c->nruns = nruns;
            ckwrite2(c);
        }
        nruns = c->nruns;
        for (int i = 0; i < nruns; i++) sprintf(runname[i], "run_%d.dat", i);
        truncate("levtmp.dat", c->outbyte);
        CW w;
        if (c->outbyte == 0) cw_open(&w, "levtmp.dat", "wb", 0, 0);
        else {
            w.f = fopen("levtmp.dat", "r+b");
            if (!w.f) { fprintf(stderr, "LEVTMP OPEN FAILED\n"); exit(3); }
            setvbuf(w.f, NULL, _IOFBF, 1 << 22);
            fseek(w.f, c->outbyte, SEEK_SET);
            w.prev = c->outprev; w.recs = 0; w.bytes = c->outbyte;
        }
        long long sumabs = 0;
        long long states = merge_append(&w, &sumabs);
        cw_close(&w);
        for (int i = 0; i < nruns; i++) remove(runname[i]);
        c->by_acc += levbytes;
        nruns = 0;
        c->st_acc += states; c->sum_acc += sumabs;
        c->outrec += states; c->outbyte = w.bytes; c->outprev = w.prev;
        c->shard++; c->phase = 0;
        c->inrec = 0; c->inbyte = 0; c->inprev = 0; c->nruns = 0;
        ckwrite2(c);
    }
    if (rename("levtmp.dat", outname) != 0) { fprintf(stderr, "LEV RENAME FAILED\n"); exit(3); }
    fprintf(stderr, "level %d: states %lld emitted %lld sum|w| %lld P %d (t %.0f)\n",
            c->lev + 1, c->st_acc, c->em_acc, c->sum_acc, c->P, difftime(time(NULL), t0));
    int nextP = (c->by_acc < BUDGET / 3 && c->P > 1) ? c->P / 2 : c->P;
    CK n = {0};
    n.lev = c->lev + 1; n.P = nextP > 0 ? nextP : 1;
    ckwrite2(&n);
    remove(inname);
    *c = n;
}

static void write_init(const char *name, uint64_t key, int64_t w) {
    CW cw; cw_open(&cw, name, "wb", 0, 0);
    cw_rec(&cw, key, w);
    cw_close(&cw);
}

static int64_t read_final(const char *name, long long *nstates) {
    CR r; cr_open(&r, name, 0, 0);
    uint64_t k; int64_t v2, v = 0; *nstates = 0;
    while (cr_rec(&r, &k, &v2)) { v = v2; (*nstates)++; }
    cr_close(&r);
    return v;
}

int main(int argc, char **argv) {
    t0 = time(NULL);
    hkey = calloc(CAPQ, sizeof(uint64_t));
    hval = malloc(CAPQ * sizeof(int64_t));
    if (!hkey || !hval) { fprintf(stderr, "alloc failed\n"); return 1; }
    char a[64], b[64];
    if (argc >= 2 && (!strcmp(argv[1], "quad") || !strcmp(argv[1], "quad0"))) {
        setup_quad(argv[1][4] == '0');
        write_init("lev0.dat", 0, 1);
        for (int c = 0; c < NF; c++) {
            sprintf(a, "lev%d.dat", c); sprintf(b, "lev%d.dat", c+1);
            do_level(a, b, c);
        }
        long long ns; int64_t v = read_final("lev4.dat", &ns);
        printf("%s VALUE %lld (final states %lld, expect 1)\n", argv[1], (long long)v, ns);
        return 0;
    }
    if (argc >= 2 && !strcmp(argv[1], "quadq")) {
        setup_quad(0);
        /* copy 0 fixed: v0 -> eps0, v3 -> eps1; sign +1; multiplier 4 */
        write_init("lev1.dat", (1ULL << 0) | (1ULL << (9 + 3)), 1);
        for (int c = 1; c < NF; c++) {
            sprintf(a, "lev%d.dat", c); sprintf(b, "lev%d.dat", c+1);
            do_level(a, b, c);
        }
        long long ns; int64_t v = read_final("lev4.dat", &ns);
        printf("quadq raw %lld x4 = %lld (final states %lld)\n", (long long)v, 4*(long long)v, ns);
        return 0;
    }
    if (argc >= 2 && (!strcmp(argv[1], "det3") || !strcmp(argv[1], "det3r")
                   || !strcmp(argv[1], "perm3") || !strcmp(argv[1], "perm3r"))) {
        int isperm = argv[1][0] == 'p';
        setup_det3(isperm);
        int rev = argv[1][strlen(argv[1])-1] == 'r';
        int maxlev = NF;
        if (argc >= 3) maxlev = atoi(argv[2]);
        /* copy 0 = diagonal root: v0->eps0, v4->eps1, v8->eps3; sign +1; x36
           (same orbit-transitivity quotient for perm3: G0 preserves perm3's
           all-positive monomial signs and the per-eps twist is sgn(g)^6 = +1) */
        uint64_t root = (1ULL << 0) | (1ULL << (9*1 + 4)) | (1ULL << (9*3 + 8));
        write_init("lev1.dat", root, 1);
        for (int lv = 1; lv < maxlev; lv++) {
            int copy = rev ? NF - lv : lv;   /* reversed order: 17,16,...,1 */
            sprintf(a, "lev%d.dat", lv); sprintf(b, "lev%d.dat", lv+1);
            do_level(a, b, copy);
            remove(a);
        }
        if (maxlev == NF) {
            long long ns; int64_t v = read_final("lev18.dat", &ns);
            printf("%s root-subtree value %lld (final states %lld, expect 1)\n", argv[1], (long long)v, ns);
            printf("PHI18(%s) pattern VALUE = 36 x %lld = %lld\n", isperm ? "perm3" : "det3", (long long)v, 36*(long long)v);
        }
        return 0;
    }
    if (argc >= 3 && (!strcmp(argv[1], "evalfile") || !strcmp(argv[1], "evalfile2"))) {
        setup_evalfile(argv[2], argv[1][8] == '2');
        char fin[64];
        if (FIXROOT >= 0) {
            uint64_t nk = 0; int64_t s = OS[0][FIXROOT];
            for (int k2 = 0; k2 < NLEG; k2++) {
                int e = OE[0][FIXROOT][k2], v = OV[0][FIXROOT][k2];
                uint64_t m = (nk >> EOFF[e]) & ((1u << EW[e]) - 1);
                if (m >> v & 1) { fprintf(stderr, "bad fixroot\n"); return 1; }
                if (__builtin_popcountll(m >> (v+1)) & 1) s = -s;
                nk |= 1ULL << (EOFF[e] + v);
            }
            write_init("lev1.dat", nk, s);
            for (int lv = 1; lv < NF; lv++) {
                sprintf(a, "lev%d.dat", lv); sprintf(b, "lev%d.dat", lv+1);
                do_level(a, b, lv);
                remove(a);
            }
        } else {
            write_init("lev0.dat", 0, 1);
            for (int lv = 0; lv < NF; lv++) {
                sprintf(a, "lev%d.dat", lv); sprintf(b, "lev%d.dat", lv+1);
                do_level(a, b, lv);
                remove(a);
            }
        }
        sprintf(fin, "lev%d.dat", NF);
        long long ns; int64_t v = read_final(fin, &ns);
        printf("evalfile %s raw %lld x mult %lld = VALUE %lld (final states %lld)\n",
               argv[2], (long long)v, FMULT, (long long)(FMULT*v), ns);
        return 0;
    }
    if (argc >= 3 && !strcmp(argv[1], "evalopts")) {
        setup_evalopts(argv[2]);
        strncpy(CKIN, argv[2], 255);
        KB = EOFF[NE-1] + EW[NE-1];
        if (getenv("DPBUDGET")) BUDGET = atof(getenv("DPBUDGET"));
        char fin[64];
        CK c;
        if (ckread2(&c)) {
            fprintf(stderr, "RESUME %s level %d P %d shard %d phase %d inrec %lld (t %.0f)\n",
                    CKIN, c.lev, c.P, c.shard, c.phase, c.inrec, difftime(time(NULL), t0));
        } else {
            memset(&c, 0, sizeof(c));
            c.P = 1;
            rmglob();
            for (int lv = 1; lv <= 24; lv++) { sprintf(a, "lev%d.dat", lv); remove(a); }
            write_init("lev0.dat", 0, 1);
            ckwrite2(&c);
        }
        while (c.lev < NF) do_level_ck2(&c);
        sprintf(fin, "lev%d.dat", NF);
        long long ns; int64_t v = read_final(fin, &ns);
        printf("evalopts %s raw %lld x mult %lld = VALUE %lld (final states %lld)\n",
               argv[2], (long long)v, FMULT, (long long)(FMULT*v), ns);
        remove("ck.txt");
        return 0;
    }
    if (argc >= 3 && !strcmp(argv[1], "det3sub")) {
        /* cross-check vs grind: root + copy1 option c fixed, DP copies 2..17 */
        setup_det3(0);
        int c1 = atoi(argv[2]);
        uint64_t root = (1ULL << 0) | (1ULL << (9*1 + 4)) | (1ULL << (9*3 + 8));
        int64_t s = OS[1][c1]; uint64_t nk = root; int ok = 1;
        for (int k2 = 0; k2 < NLEG; k2++) {
            int e = OE[1][c1][k2], v = OV[1][c1][k2];
            uint64_t m = (nk >> EOFF[e]) & ((1u << EW[e]) - 1);
            if (m >> v & 1) { ok = 0; break; }
            if (__builtin_popcountll(m >> (v+1)) & 1) s = -s;
            nk |= 1ULL << (EOFF[e] + v);
        }
        if (!ok) { printf("det3sub %d INVALID (collides with root)\n", c1); return 0; }
        write_init("lev2.dat", nk, s);
        for (int c = 2; c < NF; c++) {
            sprintf(a, "lev%d.dat", c); sprintf(b, "lev%d.dat", c+1);
            do_level(a, b, c);
            remove(a);
        }
        long long ns; int64_t v = read_final("lev18.dat", &ns);
        printf("det3sub %d partial = %lld (final states %lld)\n", c1, (long long)v, ns);
        return 0;
    }
    fprintf(stderr, "usage: dp quad|quad0|quadq|det3 [maxlev]|det3sub c\n");
    return 1;
}

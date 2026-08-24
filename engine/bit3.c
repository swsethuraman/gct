/* Order-independent signed exact-cover evaluation of the canonical pattern.
   Sign per epsilon: sgn(f-index deposit order -> sorted variables)
     = prod over deposits of (-1)^{#earlier-deposited vars > v}
       * (-1)^{#earlier-deposited f-indices > i}     (order-correction)
   Dynamic most-constrained-f ordering; resumable chunking on root options.
   Modes:  quad  = validation on 4-variable quadrics (disc pattern, 2 epsilons)
           quad0 = same at a rank-3 degenerate quadric (expect 0)
           det3  = the real thing (18 copies, 6 epsilons), args: chunk_lo chunk_hi
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

static int NF, NE, NLEG;               /* copies, epsilons, legs per copy */
static int NOPT[20];
static int OE[20][40][3], OV[20][40][3], OS[20][40];
static unsigned int vmask[8];          /* per-eps used-variable mask */
static unsigned int fmask[8];          /* per-eps depositor f-index mask */
static int cnt[8], CAP;                /* legs per epsilon when full */
static int used[20];
static int incid[8][20];               /* incid[e][i] = 1 if copy i can feed e */
static int remain[8];                  /* remaining potential suppliers per eps */
static long long total, nodes;
static time_t t0; static int budget_s = 460;
static int TAUOPT[20][40];

static void rec(int depth, long long sign, int sym) {
    nodes++;
    if ((nodes & 0xFFFFFFF) == 0)
        fprintf(stderr, "n %lld d %d t %.0f\n", nodes, depth, difftime(time(NULL), t0));
    if (depth == NF) { total += sign; return; }
    /* feasibility */
    for (int e = 0; e < NE; e++) if (CAP - cnt[e] > remain[e]) return;
    int i = depth;   /* static early-completion order set up in setup_* */
    used[i] = 1;
    for (int e = 0; e < NE; e++) remain[e] -= incid[e][i];
    for (int o = 0; o < NOPT[i]; o++) {
        long long mult = 1; int nsym = sym;
        if (sym) {
            int to = TAUOPT[i][o];
            if (to < o) continue;          /* non-canonical under tau */
            if (to > o) { mult = 2; nsym = 0; }
        }
        int ok = 1;
        for (int k = 0; k < NLEG; k++)
            if (vmask[OE[i][o][k]] >> OV[i][o][k] & 1) { ok = 0; break; }
        if (!ok) continue;
        long long s = sign * OS[i][o] * mult;
        for (int k = 0; k < NLEG; k++) {
            int e = OE[i][o][k], v = OV[i][o][k];
            int p = __builtin_popcount(vmask[e] >> (v+1))
                  + __builtin_popcount(fmask[e] >> (i+1));
            if (p & 1) s = -s;
            vmask[e] |= 1u << v; fmask[e] |= 1u << i; cnt[e]++;
        }
        rec(depth+1, s, nsym);
        for (int k = 0; k < NLEG; k++) {
            int e = OE[i][o][k], v = OV[i][o][k];
            vmask[e] &= ~(1u << OV[i][o][k]); fmask[e] &= ~(1u << i); cnt[e]--;
        }
    }
    used[i] = 0;
    for (int e = 0; e < NE; e++) remain[e] += incid[e][i];
}

static void build_tauopt(int tauv[]) {
    for (int i = 0; i < NF; i++)
        for (int o = 0; o < NOPT[i]; o++) {
            int found = -1;
            for (int o2 = 0; o2 < NOPT[i]; o2++) {
                int match = 1;
                for (int k = 0; k < NLEG; k++)
                    if (OE[i][o2][k] != OE[i][o][k] || OV[i][o2][k] != tauv[OV[i][o][k]]) { match = 0; break; }
                if (match) { found = o2; break; }
            }
            TAUOPT[i][o] = found;   /* -1 never happens for closed monomial sets */
        }
}

static void setup_det3(void) {
    NF = 18; NE = 6; NLEG = 3; CAP = 9;
    static int TRI[18][3]; int idx = 0;
    int raw[20][3]; int nraw = 0;
    for (int a = 0; a < 6; a++) for (int b = a+1; b < 6; b++) for (int c = b+1; c < 6; c++) {
        if (a==0&&b==1&&c==2) continue; if (a==3&&b==4&&c==5) continue;
        raw[nraw][0]=a; raw[nraw][1]=b; raw[nraw][2]=c; nraw++;
    }
    /* early-completion order: all triples containing 0, then remaining with 1, then with 2 */
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
            OS[i][n] = DS[m]; n++;
        }
        NOPT[i] = n;
        for (int e = 0; e < 6; e++)
            incid[e][i] = (TRI[i][0]==e||TRI[i][1]==e||TRI[i][2]==e);
    }
    for (int e = 0; e < NE; e++) { remain[e] = 0; for (int i = 0; i < NF; i++) remain[e] += incid[e][i]; }
    static int TAUV9[9] = {0,3,6,1,4,7,2,5,8};   /* transpose: 3r+c -> 3c+r */
    build_tauopt(TAUV9);
}

static void setup_quad(int degenerate) {
    /* quadrics in 4 vars, D=2: 4 copies, 2 epsilons, footprint {0,1} each.
       f = x0 x3 - x1 x2  (det2)  or  x0 x3 (rank 2, disc = 0). */
    NF = 4; NE = 2; NLEG = 2; CAP = 4;
    for (int i = 0; i < NF; i++) {
        int n = 0;
        if (!degenerate) {
            int mons[2][2] = {{0,3},{1,2}}; int ms[2] = {1, -1};
            for (int m = 0; m < 2; m++) for (int p = 0; p < 2; p++) {
                OE[i][n][0] = 0; OE[i][n][1] = 1;
                OV[i][n][0] = mons[m][p]; OV[i][n][1] = mons[m][1-p];
                OS[i][n] = ms[m]; n++;
            }
        } else {
            int mons[1][2] = {{0,3}};
            for (int p = 0; p < 2; p++) {
                OE[i][n][0] = 0; OE[i][n][1] = 1;
                OV[i][n][0] = mons[0][p]; OV[i][n][1] = mons[0][1-p];
                OS[i][n] = 1; n++;
            }
        }
        NOPT[i] = n;
        incid[0][i] = incid[1][i] = 1;
    }
    remain[0] = remain[1] = NF;
    static int TAUV4[4] = {0,2,1,3};   /* 2x2 transpose: swap x01,x10 */
    build_tauopt(TAUV4);
}

static void deposit(int e, int v, int i, long long *s) {
    int p = __builtin_popcount(vmask[e] >> (v+1)) + __builtin_popcount(fmask[e] >> (i+1));
    if (p & 1) *s = -*s;
    vmask[e] |= 1u << v; fmask[e] |= 1u << i; cnt[e]++;
}
static void undeposit(int e, int v, int i) {
    vmask[e] &= ~(1u << v); fmask[e] &= ~(1u << i); cnt[e]--;
}

int main(int argc, char **argv) {
    t0 = time(NULL);
    if (argc >= 2 && !strcmp(argv[1], "quad"))  { setup_quad(0); rec(0, 1, 0); printf("QUAD VALUE %lld nodes %lld\n", total, nodes); return 0; }
    if (argc >= 2 && !strcmp(argv[1], "quad0")) { setup_quad(1); rec(0, 1, 0); printf("QUAD0 VALUE %lld nodes %lld\n", total, nodes); return 0; }
    if (argc >= 2 && !strcmp(argv[1], "tau1")) {
        setup_det3();
        for (int c = 0; c < NOPT[1]; c++) printf("%d:%d ", c, TAUOPT[1][c]);
        printf("\n"); return 0;
    }
    if (argc >= 2 && !strcmp(argv[1], "quadq")) {
        /* quotient validation: fix copy 0 = diagonal option (v0->eps0, v3->eps1), multiply by 4 */
        setup_quad(0);
        long long s = 1;
        used[0] = 1; remain[0]--; remain[1]--;
        deposit(0, 0, 0, &s); deposit(1, 3, 0, &s);
        rec(1, s, 1);   /* root option is tau-fixed; tau-canonicity bakes the x2 into mult */
        printf("QUADQ raw %lld x4 = %lld nodes %lld (expect 24)\n", total, 4*total, nodes);
        return 0;
    }
    if (argc >= 2 && !strcmp(argv[1], "det3q")) {
        /* symmetry-quotiented run: copy 0 fixed to the diagonal option
           (identity monomial, vars 0,4,8 -> eps 0,1,3); final value = 36 x subtree.
           sub-chunks on copy 1's options, args: lo hi budget. */
        setup_det3();
        int lo = 0, hi = NOPT[1];
        if (argc >= 4) { lo = atoi(argv[2]); hi = atoi(argv[3]); }
        if (argc >= 5) budget_s = atoi(argv[4]);
        long long s0 = 1;
        used[0] = 1;
        for (int e = 0; e < NE; e++) remain[e] -= incid[e][0];
        deposit(0, 0, 0, &s0); deposit(1, 4, 0, &s0); deposit(3, 8, 0, &s0);
        used[1] = 1;
        for (int e = 0; e < NE; e++) remain[e] -= incid[e][1];
        for (int c = lo; c < hi; c++) {
            if (difftime(time(NULL), t0) > budget_s) { printf("STOPPED before subchunk %d\n", c); return 2; }
            long long save = total;
            int tc = TAUOPT[1][c];
            if (tc < c) {   /* tau-image of an earlier sub-chunk; its weight is banked there */
                printf("SUB %d partial 0 cum %lld nodes %lld t %.0f (tau-dup of %d)\n",
                       c, total, nodes, difftime(time(NULL), t0), tc);
                fflush(stdout);
                continue;
            }
            long long mult = (tc > c) ? 2 : 1;
            int nsym = (tc == c) ? 1 : 0;
            int ok = 1;
            for (int k = 0; k < NLEG; k++)
                if (vmask[OE[1][c][k]] >> OV[1][c][k] & 1) { ok = 0; break; }
            if (ok) {
                long long s = s0 * OS[1][c] * mult;
                for (int k = 0; k < NLEG; k++) deposit(OE[1][c][k], OV[1][c][k], 1, &s);
                rec(2, s, nsym);
                for (int k = 0; k < NLEG; k++) undeposit(OE[1][c][k], OV[1][c][k], 1);
            }
            printf("SUB %d partial %lld cum %lld nodes %lld t %.0f\n",
                   c, total - save, total, nodes, difftime(time(NULL), t0));
            fflush(stdout);
        }
        printf("RANGE DONE [%d,%d) cum %lld nodes %lld  => if full range: VALUE = 36 x cum = %lld\n",
               lo, hi, total, nodes, 36*total);
        return 0;
    }
    setup_det3();
    int lo = 0, hi = NOPT[0];
    if (argc >= 4) { lo = atoi(argv[2]); hi = atoi(argv[3]); }
    if (argc >= 5) budget_s = atoi(argv[4]);
    /* chunk on copy 0's options: fix copy 0 = option c, search the rest */
    for (int c = lo; c < hi; c++) {
        if (difftime(time(NULL), t0) > budget_s) { printf("STOPPED before chunk %d\n", c); return 2; }
        long long save_total = total;
        int i = 0; used[0] = 1;
        for (int e = 0; e < NE; e++) remain[e] -= incid[e][0];
        int o = c, ok = 1;
        for (int k = 0; k < NLEG; k++) if (vmask[OE[i][o][k]] >> OV[i][o][k] & 1) ok = 0;
        if (ok) {
            long long s = OS[i][o];
            for (int k = 0; k < NLEG; k++) {
                int e = OE[i][o][k], v = OV[i][o][k];
                int p = __builtin_popcount(vmask[e] >> (v+1)) + __builtin_popcount(fmask[e] >> 1);
                if (p & 1) s = -s;
                vmask[e] |= 1u << v; fmask[e] |= 1u << 0; cnt[e]++;
            }
            rec(1, s, 0);
            for (int k = 0; k < NLEG; k++) {
                int e = OE[i][o][k];
                vmask[e] &= ~(1u << OV[i][o][k]); fmask[e] &= ~1u; cnt[e]--;
            }
        }
        used[0] = 0;
        for (int e = 0; e < NE; e++) remain[e] += incid[e][0];
        printf("CHUNK %d partial %lld cumulative %lld nodes %lld t %.0f\n",
               c, total - save_total, total, nodes, difftime(time(NULL), t0));
        fflush(stdout);
    }
    printf("DONE range [%d,%d) cumulative %lld nodes %lld\n", lo, hi, total, nodes);
    return 0;
}

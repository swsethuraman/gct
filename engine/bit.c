/* Canonical-pattern evaluation of the unique degree-18 invariant at det_3.
   18 f-copies with distinct epsilon-triples (C(6,3) minus complementary pair),
   signed exact-cover backtracking with insertion parities. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

static int TRI[18][3];
static int OPT_N[18];
static int OPT_E[18][40][3], OPT_V[18][40][3], OPT_S[18][40];
static int REMAIN[19][6];
static unsigned short mask[6];
static int cnt[6];
static long long total = 0, nodes = 0;
static time_t t0;

static const int DM[6][3] = { {0,4,8},{0,5,7},{1,3,8},{1,5,6},{2,3,7},{2,4,6} };
static const int DS[6]     = { 1, -1, -1, 1, 1, -1 };
/* signs: det = sum sgn(sigma) x_{0,s0} x_{1,s1} x_{2,s2}; var index 3r+c.
   (012)->id +, (0,5,7)= sigma mapping rows(0,1,2)->cols(0,2,1): odd -,
   (1,3,8): cols(1,0,2): odd -, (1,5,6): cols(1,2,0): even +,
   (2,3,7): cols(2,0,1): even +, (2,4,6): cols(2,1,0): odd -   */

static void rec(int pos, int sign) {
    nodes++;
    if ((nodes & 0xFFFFFFF) == 0) {
        fprintf(stderr, "nodes %lld (%.0fs) pos %d\n", nodes, difftime(time(NULL), t0), pos);
    }
    if (pos == 18) { total += sign; return; }
    for (int e = 0; e < 6; e++)
        if (9 - cnt[e] > REMAIN[pos][e]) return;
    int n = OPT_N[pos];
    for (int o = 0; o < n; o++) {
        int ok = 1;
        for (int k = 0; k < 3; k++)
            if (mask[OPT_E[pos][o][k]] >> OPT_V[pos][o][k] & 1) { ok = 0; break; }
        if (!ok) continue;
        int s = sign * OPT_S[pos][o];
        for (int k = 0; k < 3; k++) {
            int e = OPT_E[pos][o][k], v = OPT_V[pos][o][k];
            s *= (__builtin_popcount(mask[e] >> (v+1)) & 1) ? -1 : 1;
            mask[e] |= 1 << v; cnt[e]++;
        }
        rec(pos+1, s);
        for (int k = 0; k < 3; k++) {
            int e = OPT_E[pos][o][k], v = OPT_V[pos][o][k];
            mask[e] &= ~(1 << v); cnt[e]--;
        }
    }
}

int main(void) {
    t0 = time(NULL);
    int idx = 0;
    for (int a = 0; a < 6; a++) for (int b = a+1; b < 6; b++) for (int c = b+1; c < 6; c++) {
        if (a==0&&b==1&&c==2) continue;
        if (a==3&&b==4&&c==5) continue;
        TRI[idx][0]=a; TRI[idx][1]=b; TRI[idx][2]=c; idx++;
    }
    if (idx != 18) { printf("bad triples\n"); return 1; }
    /* order: lexicographic (already) */
    for (int i = 0; i < 18; i++) {
        int n = 0;
        for (int m = 0; m < 6; m++) {
            static const int P[6][3] = {{0,1,2},{0,2,1},{1,0,2},{1,2,0},{2,0,1},{2,1,0}};
            for (int p = 0; p < 6; p++) {
                for (int k = 0; k < 3; k++) {
                    OPT_E[i][n][k] = TRI[i][k];
                    OPT_V[i][n][k] = DM[m][P[p][k]];
                }
                OPT_S[i][n] = DS[m];
                n++;
            }
        }
        OPT_N[i] = n; /* 36 */
    }
    memset(REMAIN, 0, sizeof REMAIN);
    for (int pos = 17; pos >= 0; pos--)
        for (int e = 0; e < 6; e++)
            REMAIN[pos][e] = REMAIN[pos+1][e] + ((TRI[pos][0]==e||TRI[pos][1]==e||TRI[pos][2]==e)?1:0);
    rec(0, 1);
    printf("nodes %lld\n", nodes);
    printf("VALUE %lld\n", total);
    return 0;
}

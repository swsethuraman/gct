/* br.c - exact bracket-monomial evaluator for cubics supported on the six
   3x3 permutation monomials (the space U spanned by prod_i x_{i,sigma(i)}).

   Input spec (stdin or file):
       NB NL
       <NL lines: b0 b1 b2>          brackets of each letter, in DP order
       u0 u1 u2 u3 u4 u5             weights of the six permutations,
                                     order = itertools.permutations((0,1,2))

   Computes  V = sum over all assignments (per letter: a permutation sigma and
   a bijection of its three cells to its three brackets) of
       prod_j u_{sigma_j}  *  prod_b sgn(beta_b)
   where beta_b is the bijection (letters of b, in DP order) -> cells, and the
   cell of row r is (r, sigma(r)) packed as 3r+c.  V = 6^NL * B(S)(F).

   State = the 9-bit used-cell masks of the PARTIALLY filled brackets only
   (empty -> 0, full -> 511 are implicit), packed 9 bits each into a u64.
   Exact __int128 accumulation; open addressing with linear probing.
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

static int NB, NL;
static int TRI[32][3];
static long long U[6];

static int PERM[6][3];
static int dfill[32][9];     /* dfill[L][b] = #cells in bracket b after L letters */
static int part[32][9], npart[32];
static int slot[32][9];      /* slot[L][b] = index in the packed key, or -1 */

typedef struct { uint64_t key; __int128 val; } Ent;
static Ent *TA, *TB;
static uint64_t MASKSZ;      /* power of two */
static uint64_t *usedA, *usedB;   /* occupancy bitmaps */

static uint64_t mix(uint64_t x){ x^=x>>33; x*=0xff51afd7ed558ccdULL; x^=x>>33; x*=0xc4ceb9fe1a85ec53ULL; x^=x>>33; return x; }

static uint64_t nA, nB;

static void tinit(Ent *T, uint64_t *used){ memset(used,0,(MASKSZ/64)*8); (void)T; }

static void tadd(Ent *T, uint64_t *used, uint64_t *cnt, uint64_t key, __int128 v){
    uint64_t h = mix(key) & (MASKSZ-1);
    for(;;){
        if(!((used[h>>6]>>(h&63))&1ULL)){
            used[h>>6] |= 1ULL<<(h&63);
            T[h].key = key; T[h].val = v; (*cnt)++;
            if(*cnt > (MASKSZ*3)/4){ fprintf(stderr,"TABLE FULL (%llu)\n",(unsigned long long)*cnt); exit(2); }
            return;
        }
        if(T[h].key == key){ T[h].val += v; return; }
        h = (h+1)&(MASKSZ-1);
    }
}

int main(int argc, char **argv){
    FILE *f = stdin;
    if(argc>1){ f = fopen(argv[1],"r"); if(!f){perror("open");return 1;} }
    int lg = (argc>2)? atoi(argv[2]) : 26;
    if(fscanf(f,"%d %d",&NB,&NL)!=2){fprintf(stderr,"bad header\n");return 1;}
    for(int j=0;j<NL;j++) if(fscanf(f,"%d %d %d",&TRI[j][0],&TRI[j][1],&TRI[j][2])!=3){fprintf(stderr,"bad tri\n");return 1;}
    for(int i=0;i<6;i++) if(fscanf(f,"%lld",&U[i])!=1){fprintf(stderr,"bad u\n");return 1;}
    if(f!=stdin) fclose(f);

    { int p[3]={0,1,2}, n=0;
      int idx[6][3]={{0,1,2},{0,2,1},{1,0,2},{1,2,0},{2,0,1},{2,1,0}};
      for(n=0;n<6;n++) for(int k=0;k<3;k++) PERM[n][k]=idx[n][k];
      (void)p; }

    /* fills and packing per level */
    for(int b=0;b<NB;b++) dfill[0][b]=0;
    for(int L=1;L<=NL;L++){
        for(int b=0;b<NB;b++) dfill[L][b]=dfill[L-1][b];
        for(int k=0;k<3;k++) dfill[L][TRI[L-1][k]]++;
    }
    for(int L=0;L<=NL;L++){
        npart[L]=0;
        for(int b=0;b<NB;b++){
            slot[L][b] = -1;
            if(dfill[L][b]>0 && dfill[L][b]<9){ slot[L][b]=npart[L]; part[L][npart[L]++]=b; }
        }
        if(npart[L]*9 > 63){ fprintf(stderr,"level %d needs %d partial brackets (>7)\n",L,npart[L]); return 3; }
    }
    for(int b=0;b<NB;b++) if(dfill[NL][b]!=9){ fprintf(stderr,"bracket %d has %d letters, need 9\n",b,dfill[NL][b]); return 4; }

    MASKSZ = 1ULL<<lg;
    TA = malloc(MASKSZ*sizeof(Ent)); TB = malloc(MASKSZ*sizeof(Ent));
    usedA = malloc((MASKSZ/64)*8); usedB = malloc((MASKSZ/64)*8);
    if(!TA||!TB||!usedA||!usedB){fprintf(stderr,"alloc failed\n");return 5;}

    tinit(TA,usedA); nA=0;
    tadd(TA,usedA,&nA,0ULL,(__int128)1);
    time_t t0=time(NULL);

    for(int L=1;L<=NL;L++){
        tinit(TB,usedB); nB=0;
        int *tri = TRI[L-1];
        unsigned long long emitted=0;
        for(uint64_t h=0; h<MASKSZ; h++){
            if(!((usedA[h>>6]>>(h&63))&1ULL)) continue;
            __int128 v = TA[h].val;
            if(v==0) continue;
            uint64_t key = TA[h].key;
            int m[9];
            for(int b=0;b<NB;b++){
                int s = slot[L-1][b];
                m[b] = (s<0) ? (dfill[L-1][b]==0 ? 0 : 511) : (int)((key>>(9*s)) & 511u);
            }
            for(int pi=0; pi<6; pi++){
                /* row assigned to tri[k] is PERM[pi][k] */
                for(int si=0; si<6; si++){
                    long long w = U[si];
                    if(w==0) continue;
                    int nm[3]; int sgn=1; int ok=1;
                    for(int k=0;k<3;k++){
                        int r = PERM[pi][k];
                        int c = PERM[si][r];
                        int cell = 3*r+c;
                        int b = tri[k];
                        int mm = m[b];
                        if((mm>>cell)&1){ ok=0; break; }
                        int hi = __builtin_popcount((unsigned)(mm >> (cell+1)));
                        if(hi&1) sgn=-sgn;
                        nm[k] = mm | (1<<cell);
                    }
                    if(!ok) continue;
                    int mm2[9];
                    for(int b=0;b<NB;b++) mm2[b]=m[b];
                    for(int k=0;k<3;k++) mm2[tri[k]] = nm[k];
                    uint64_t nk=0;
                    for(int s=0;s<npart[L];s++) nk |= ((uint64_t)mm2[part[L][s]]) << (9*s);
                    tadd(TB,usedB,&nB,nk,v*(__int128)(sgn*w));
                    emitted++;
                }
            }
        }
        { Ent *t=TA; TA=TB; TB=t; uint64_t *u=usedA; usedA=usedB; usedB=u; nA=nB; }
        /* drop zeros lazily: count nonzero */
        uint64_t nz=0;
        for(uint64_t h=0;h<MASKSZ;h++) if(((usedA[h>>6]>>(h&63))&1ULL) && TA[h].val!=0) nz++;
        fprintf(stderr,"level %2d: partial=%d states=%llu nonzero=%llu emitted=%llu  %lds\n",
                L,npart[L],(unsigned long long)nA,(unsigned long long)nz,emitted,(long)(time(NULL)-t0));
    }
    /* final state: all full -> key 0, npart=0 */
    __int128 res=0;
    for(uint64_t h=0;h<MASKSZ;h++) if(((usedA[h>>6]>>(h&63))&1ULL)) res += TA[h].val;
    /* print __int128 */
    { char buf[64]; int i=63; buf[i--]=0; int neg = res<0; unsigned __int128 x = neg? (unsigned __int128)(-res) : (unsigned __int128)res;
      if(x==0) buf[i--]='0';
      while(x){ buf[i--] = '0'+(int)(x%10); x/=10; }
      if(neg) buf[i--]='-';
      printf("VALUE %s\n", buf+i+1); }
    return 0;
}

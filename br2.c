/* br2.c - exact bracket-monomial evaluator for cubics supported on the six
   3x3 permutation monomials.  Streamed level DP, exact __int128 arithmetic.

   spec file:
       NB NL
       NL lines: b0 b1 b2        (brackets of each letter, in DP order)
       u0 .. u5                  (weights of the six permutations, in
                                  itertools.permutations((0,1,2)) order)

   State = the 9-bit used-cell masks of the PARTIALLY filled brackets, packed
   9 bits each into a u64 (empty -> 0 and full -> 511 are implicit).
   Per level: P sharded passes over the previous level file, each pass keeping
   only target keys with (mix(key) mod P) == p, so the in-RAM table never
   overflows; P doubles and the level restarts if it does.

   usage: br2 spec.txt [log2 table slots] [scratchdir]
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

static int NB, NL;
static int TRI[32][3];
static long long U[6];
static int PERM[6][3] = {{0,1,2},{0,2,1},{1,0,2},{1,2,0},{2,0,1},{2,1,0}};
static int dfill[33][9], part[33][9], npart[33], slotix[33][9];

typedef struct __attribute__((packed)) { uint64_t key; __int128 val; } Rec;

static uint64_t MASKSZ, CAP;
static uint64_t *tk;          /* key+1, 0 = empty */
static __int128 *tv;
static uint64_t ncur;
static char SCRATCH[512] = ".";

static inline uint64_t mix(uint64_t x){ x^=x>>33; x*=0xff51afd7ed558ccdULL; x^=x>>33; x*=0xc4ceb9fe1a85ec53ULL; x^=x>>33; return x; }

static int tadd(uint64_t key, __int128 v){
    uint64_t h = mix(key) & (MASKSZ-1);
    for(;;){
        uint64_t k = tk[h];
        if(k == 0){
            if(ncur >= CAP) return 0;          /* overflow: caller restarts */
            tk[h] = key+1; tv[h] = v; ncur++; return 1;
        }
        if(k == key+1){ tv[h] += v; return 1; }
        h = (h+1)&(MASKSZ-1);
    }
}

static void path(char *dst, const char *name){ snprintf(dst, 600, "%s/%s", SCRATCH, name); }

int main(int argc, char **argv){
    if(argc<2){ fprintf(stderr,"usage: br2 spec [lgslots] [scratch]\n"); return 1; }
    FILE *f = fopen(argv[1],"r"); if(!f){perror("spec");return 1;}
    int lg = (argc>2)? atoi(argv[2]) : 27;
    if(argc>3) snprintf(SCRATCH,sizeof SCRATCH,"%s",argv[3]);
    if(fscanf(f,"%d %d",&NB,&NL)!=2) return 1;
    for(int j=0;j<NL;j++) if(fscanf(f,"%d %d %d",&TRI[j][0],&TRI[j][1],&TRI[j][2])!=3) return 1;
    for(int i=0;i<6;i++) if(fscanf(f,"%lld",&U[i])!=1) return 1;
    fclose(f);

    for(int b=0;b<NB;b++) dfill[0][b]=0;
    for(int L=1;L<=NL;L++){
        for(int b=0;b<NB;b++) dfill[L][b]=dfill[L-1][b];
        for(int k=0;k<3;k++) dfill[L][TRI[L-1][k]]++;
    }
    for(int L=0;L<=NL;L++){
        npart[L]=0;
        for(int b=0;b<NB;b++){
            slotix[L][b]=-1;
            if(dfill[L][b]>0 && dfill[L][b]<9){ slotix[L][b]=npart[L]; part[L][npart[L]++]=b; }
        }
        if(npart[L]*9 > 63){ fprintf(stderr,"level %d: %d partial brackets\n",L,npart[L]); return 3; }
    }
    for(int b=0;b<NB;b++) if(dfill[NL][b]!=9){ fprintf(stderr,"bracket %d fill %d\n",b,dfill[NL][b]); return 4; }

    MASKSZ = 1ULL<<lg; CAP = (MASKSZ*3)/4;
    tk = calloc(MASKSZ,8); tv = malloc(MASKSZ*sizeof(__int128));
    if(!tk||!tv){fprintf(stderr,"alloc\n");return 5;}

    char pcur[600], pnxt[600];
    path(pcur,"lev_cur.bin"); path(pnxt,"lev_nxt.bin");
    { FILE *g=fopen(pcur,"wb"); Rec r; r.key=0; r.val=1; fwrite(&r,sizeof r,1,g); fclose(g); }
    time_t t0=time(NULL);
    unsigned long long curstates = 1;

    for(int L=1;L<=NL;L++){
        int *tri = TRI[L-1];
        int P = 1;
        unsigned long long nxtstates=0, emitted=0;
        for(;;){
            FILE *out = fopen(pnxt,"wb");
            if(!out){perror("out");return 6;}
            nxtstates=0; emitted=0;
            int restart=0;
            for(int p=0;p<P && !restart;p++){
                memset(tk,0,MASKSZ*8); ncur=0;
                FILE *in = fopen(pcur,"rb"); if(!in){perror("in");return 6;}
                Rec buf[4096]; size_t got;
                while((got=fread(buf,sizeof(Rec),4096,in))>0 && !restart){
                    for(size_t ii=0; ii<got; ii++){
                        __int128 v = buf[ii].val; if(v==0) continue;
                        uint64_t key = buf[ii].key;
                        int m[9];
                        for(int b=0;b<NB;b++){
                            int s=slotix[L-1][b];
                            m[b] = (s<0) ? (dfill[L-1][b]==0?0:511) : (int)((key>>(9*s))&511u);
                        }
                        for(int pi=0;pi<6;pi++) for(int si=0;si<6;si++){
                            long long w=U[si]; if(w==0) continue;
                            int nm[3], sgn=1, ok=1;
                            for(int k=0;k<3;k++){
                                int r=PERM[pi][k], c=PERM[si][r], cell=3*r+c, b=tri[k], mm=m[b];
                                if((mm>>cell)&1){ ok=0; break; }
                                if(__builtin_popcount((unsigned)(mm>>(cell+1)))&1) sgn=-sgn;
                                nm[k]= mm|(1<<cell);
                            }
                            if(!ok) continue;
                            uint64_t nk=0;
                            for(int s=0;s<npart[L];s++){
                                int b=part[L][s];
                                int mv=m[b];
                                for(int k=0;k<3;k++) if(tri[k]==b) mv=nm[k];
                                nk |= ((uint64_t)mv)<<(9*s);
                            }
                            if(P>1 && (mix(nk)%(uint64_t)P)!=(uint64_t)p) continue;
                            emitted++;
                            if(!tadd(nk, v*(__int128)(sgn*w))){ restart=1; break; }
                        }
                        if(restart) break;
                    }
                }
                fclose(in);
                if(restart) break;
                /* flush table to out */
                for(uint64_t h=0;h<MASKSZ;h++) if(tk[h] && tv[h]!=0){
                    Rec r; r.key=tk[h]-1; r.val=tv[h];
                    fwrite(&r,sizeof r,1,out); nxtstates++;
                }
            }
            fclose(out);
            if(!restart) break;
            P*=2;
            fprintf(stderr,"  level %d: table overflow, retry with P=%d\n",L,P);
            if(P>64){ fprintf(stderr,"too many shards\n"); return 7; }
        }
        rename(pnxt,pcur);
        curstates=nxtstates;
        fprintf(stderr,"level %2d: partial=%d P=%d states=%llu emitted=%llu  %lds\n",
                L,npart[L],P,nxtstates,emitted,(long)(time(NULL)-t0));
        fflush(stderr);
    }
    __int128 res=0;
    { FILE *in=fopen(pcur,"rb"); Rec r; while(fread(&r,sizeof r,1,in)==1) res+=r.val; fclose(in); }
    { char buf[64]; int i=63; buf[i--]=0; int neg=res<0; unsigned __int128 x = neg?(unsigned __int128)(-res):(unsigned __int128)res;
      if(!x) buf[i--]='0'; while(x){ buf[i--]='0'+(int)(x%10); x/=10; } if(neg) buf[i--]='-';
      printf("VALUE %s\n", buf+i+1); }
    (void)curstates;
    return 0;
}

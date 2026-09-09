/* B13-01 -- exact count of multisets of 13 cubic exponent vectors (|beta|=3, 9 vars)
 * summing to a given weight `target` (sum 39).  Used for the cubic-plethysm Weyl
 * alternation  a3(mu,13) = sum_w sgn(w) m(w(mu+rho)-rho),  m = this count.
 *
 * Batch interface: reads on stdin  "N\n" then N lines of 9 ints; prints N counts.
 * DP over cubic types in fixed order with a per-target generation-stamped hash memo.
 * Counts fit in int64 (largest weight-space dim here ~8.1e8 << 2^63).
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

typedef long long i64;
typedef unsigned long long u64;

static int CUB[512][9];      /* the 165 cubic vectors */
static int NC;

static void gen_cubics(void) {
    NC = 0;
    for (int a0=3;a0>=0;a0--) for (int a1=3-a0;a1>=0;a1--) for (int a2=3-a0-a1;a2>=0;a2--)
     for (int a3=3-a0-a1-a2;a3>=0;a3--) for (int a4=3-a0-a1-a2-a3;a4>=0;a4--)
      for (int a5=3-a0-a1-a2-a3-a4;a5>=0;a5--) for (int a6=3-a0-a1-a2-a3-a4-a5;a6>=0;a6--)
       for (int a7=3-a0-a1-a2-a3-a4-a5-a6;a7>=0;a7--){
         int a8=3-a0-a1-a2-a3-a4-a5-a6-a7;
         int *c=CUB[NC]; c[0]=a0;c[1]=a1;c[2]=a2;c[3]=a3;c[4]=a4;c[5]=a5;c[6]=a6;c[7]=a7;c[8]=a8;
         NC++;
       }
}

/* shared global hash memo (rec(i,k,rem) is target-independent, so shareable across all weights) */
#define HBITS 27
#define HSIZE (1ULL<<HBITS)
#define HMASK (HSIZE-1)
static u64 *hkey; static i64 *hval; static uint8_t *hused;

static inline u64 mix(u64 x){ x^=x>>33; x*=0xff51afd7ed558ccdULL; x^=x>>33; x*=0xc4ceb9fe1a85ec53ULL; x^=x>>33; return x; }

/* key: i (9 bits) | k (4 bits) | rem packed 9*5 bits.  rem coords < 32 (max weight 29). */
static inline u64 mkkey(int i,int k,const int*rem){
    u64 key=((u64)i<<49)|((u64)k<<45);
    for(int c=0;c<9;c++) key|=((u64)(rem[c]&31))<<(5*c);
    return key;
}
static inline int hget(u64 key,i64*out){
    u64 h=mix(key)&HMASK;
    while(hused[h]){ if(hkey[h]==key){*out=hval[h];return 1;} h=(h+1)&HMASK; }
    return 0;
}
static inline void hput(u64 key,i64 v){
    u64 h=mix(key)&HMASK;
    while(hused[h]){ if(hkey[h]==key){hval[h]=v;return;} h=(h+1)&HMASK; }
    hused[h]=1; hkey[h]=key; hval[h]=v;
}

static i64 rec(int i,int k,int*rem){
    if(k==0){ for(int c=0;c<9;c++) if(rem[c]) return 0; return 1; }
    if(i==NC) return 0;
    int s=0; for(int c=0;c<9;c++) s+=rem[c];
    if(s!=3*k) return 0;
    u64 key=mkkey(i,k,rem); i64 memo;
    if(hget(key,&memo)) return memo;
    int *a=CUB[i]; int maxm=k;
    for(int c=0;c<9;c++){ if(a[c]){ int q=rem[c]/a[c]; if(q<maxm) maxm=q; } }
    i64 tot=0; int nrem[9];
    for(int m=0;m<=maxm;m++){
        for(int c=0;c<9;c++) nrem[c]=rem[c]-m*a[c];
        tot+=rec(i+1,k-m,nrem);
    }
    hput(key,tot);
    return tot;
}

int main(void){
    gen_cubics();
    if(NC!=165){ fprintf(stderr,"NC=%d expected 165\n",NC); return 2; }
    hkey=malloc(sizeof(u64)*HSIZE); hval=malloc(sizeof(i64)*HSIZE);
    hused=calloc(HSIZE,sizeof(uint8_t));
    if(!hkey||!hval||!hused){ fprintf(stderr,"alloc fail\n"); return 3; }
    int N; if(scanf("%d",&N)!=1) return 1;
    for(int t=0;t<N;t++){
        int rem[9]; int s=0;
        for(int c=0;c<9;c++){ if(scanf("%d",&rem[c])!=1) return 1; s+=rem[c]; }
        i64 v=0;
        if(s==39){ int neg=0; for(int c=0;c<9;c++) if(rem[c]<0) neg=1;
                   if(!neg) v=rec(0,13,rem); }
        printf("%lld\n",v);
        if((t&255)==0) fprintf(stderr,"\r%d/%d",t,N);
    }
    fprintf(stderr,"\n");
    return 0;
}

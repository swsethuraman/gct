#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef long long i64; typedef unsigned long long u64;
static int Q[600][9]; static int NQ;
static void gen(){NQ=0;
 for(int a0=4;a0>=0;a0--)for(int a1=4-a0;a1>=0;a1--)for(int a2=4-a0-a1;a2>=0;a2--)
 for(int a3=4-a0-a1-a2;a3>=0;a3--)for(int a4=4-a0-a1-a2-a3;a4>=0;a4--)
 for(int a5=4-a0-a1-a2-a3-a4;a5>=0;a5--)for(int a6=4-a0-a1-a2-a3-a4-a5;a6>=0;a6--)
 for(int a7=4-a0-a1-a2-a3-a4-a5-a6;a7>=0;a7--){int a8=4-a0-a1-a2-a3-a4-a5-a6-a7;
 int*c=Q[NQ];c[0]=a0;c[1]=a1;c[2]=a2;c[3]=a3;c[4]=a4;c[5]=a5;c[6]=a6;c[7]=a7;c[8]=a8;NQ++;}}
#define HB 27
#define HS (1ULL<<HB)
static u64*hk; static i64*hv; static uint8_t*hu;
static inline u64 mix(u64 x){x^=x>>33;x*=0xff51afd7ed558ccdULL;x^=x>>33;x*=0xc4ceb9fe1a85ec53ULL;x^=x>>33;return x;}
static inline u64 mk(int i,int k,const int*r){u64 K=((u64)i<<49)|((u64)k<<45);for(int c=0;c<9;c++)K|=((u64)(r[c]&31))<<(5*c);return K;}
static i64 rec(int i,int k,int*r){
 if(k==0){for(int c=0;c<9;c++)if(r[c])return 0;return 1;}
 if(i==NQ)return 0; int s=0;for(int c=0;c<9;c++)s+=r[c]; if(s!=4*k)return 0;
 u64 key=mk(i,k,r),h=mix(key)&(HS-1);
 while(hu[h]){if(hk[h]==key)return hv[h];h=(h+1)&(HS-1);}
 int*a=Q[i],mm=k; for(int c=0;c<9;c++)if(a[c]){int q=r[c]/a[c];if(q<mm)mm=q;}
 i64 t=0; int nr[9]; for(int m=0;m<=mm;m++){for(int c=0;c<9;c++)nr[c]=r[c]-m*a[c];t+=rec(i+1,k-m,nr);}
 h=mix(key)&(HS-1); while(hu[h]){if(hk[h]==key){hv[h]=t;return t;}h=(h+1)&(HS-1);} hu[h]=1;hk[h]=key;hv[h]=t; return t;}
int main(){gen(); if(NQ!=495){printf("NQ=%d\n",NQ);return 2;}
 hk=malloc(8*HS);hv=malloc(8*HS);hu=calloc(HS,1);
 int r[9]={21,17,2,2,2,2,2,2,2}; printf("N_S(21,17,2^7;13) = %lld\n", rec(0,13,r)); return 0;}

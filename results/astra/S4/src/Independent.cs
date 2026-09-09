using System;
using System.Collections.Generic;
public sealed class S4Stage {
 public int ina,inb,oldN,newN,branches,degree;
 public int[] bits,states,signs;
 public long[] tensor;
}
public static class S4Independent {
 static int Pop(int x){int n=0;while(x>0){x&=x-1;n++;}return n;}
 static int[] Masks(int h,int k){var a=new List<int>();for(int m=0;m<(1<<h);m++)if(Pop(m)==k)a.Add(m);return a.ToArray();}
 public static long Run(int h,long p,S4Stage[] stages){
  int ka=0,kb=0;long[] cur=new long[]{1};int[] aa=new int[]{0},bb=new int[]{0};int full=(1<<h)-1;
  foreach(var t in stages){
   var an=Masks(h,ka+t.ina);var bn=Masks(h,kb+t.inb);
   int[] ai=new int[1<<h],bi=new int[1<<h];for(int z=0;z<an.Length;z++)ai[an[z]]=z;for(int z=0;z<bn.Length;z++)bi[bn[z]]=z;
   long[] next=new long[an.Length*bn.Length*t.newN];int tj=t.inb==1?h:1;
   for(int ax=0;ax<aa.Length;ax++)for(int bx=0;bx<bb.Length;bx++)for(int state=0;state<t.oldN;state++){
    long v=cur[(ax*bb.Length+bx)*t.oldN+state];if(v==0)continue;
    int am=t.ina==1?full^aa[ax]:1,bm0=t.inb==1?full^bb[bx]:1;
    while(am!=0){int ab=am&-am;am-=ab;int i=Pop(ab-1),amask=t.ina==1?aa[ax]|ab:aa[ax];int asg=t.ina==1?Pop(aa[ax]>>(i+1))&1:0;
     int bm=bm0;while(bm!=0){int bit=bm&-bm;bm-=bit;int j=Pop(bit-1),bmask=t.inb==1?bb[bx]|bit:bb[bx];int bsg=t.inb==1?Pop(bb[bx]>>(j+1))&1:0;
      for(int branch=0;branch<t.branches;branch++){
       int k=state*t.branches+branch;long symbol=t.tensor[((i*tj+j)<<t.degree)+t.bits[k]];
       long add=v*symbol%p;if((asg^bsg^t.signs[k])!=0 && add!=0)add=p-add;
       int dest=(ai[amask]*bn.Length+bi[bmask])*t.newN+t.states[k];next[dest]+=add;if(next[dest]>=p)next[dest]-=p;
      }
     }
    }
   }
   cur=next;aa=an;bb=bn;ka+=t.ina;kb+=t.inb;
  }
  if(cur.Length!=1)throw new Exception("uncontracted state");return cur[0];
 }
}

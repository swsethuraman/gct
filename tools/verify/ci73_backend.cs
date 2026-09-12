// CI73 independent, batched frontier contraction. C# 5 / .NET Framework 4.
// No producer evaluator or native library is used. See ci73_proof.md.
using System;
using System.IO;
using System.Linq;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.Numerics;
using System.Web.Script.Serialization;

public static class CI73Backend {
    static int Pop(int x) { int n=0; while(x!=0){x&=x-1;n++;}return n; }
    static int[] Ints(object x) { return ((IEnumerable)x).Cast<object>().Select(Convert.ToInt32).ToArray(); }
    static int[][] Rows(object x) { return ((IEnumerable)x).Cast<object>().Select(Ints).ToArray(); }
    static int Choose(int n,int k) { if(k<0||k>n)return 0; int v=1; for(int i=1;i<=k;i++)v=v*(n-i+1)/i;return v; }
    struct Option { public int Row, Rank, Sign; public Option(int i,int r,int s){Row=i;Rank=r;Sign=s;} }
    struct Edge { public int Local, Next, Sign; public Edge(int l,int n,int s){Local=l;Next=n;Sign=s;} }
    static Option[][] Options(int[] masks,bool use,int h,int[] rank) {
        var all=new Option[masks.Length][];
        for(int k=0;k<masks.Length;k++){
            if(!use){all[k]=new[]{new Option(0,k,1)};continue;}
            var a=new List<Option>();
            for(int i=0;i<h;i++)if((masks[k]&(1<<i))==0)
                a.Add(new Option(i,rank[masks[k]|(1<<i)],(Pop(masks[k]>>(i+1))&1)==0?1:-1));
            all[k]=a.ToArray();
        }return all;
    }
    // In Z/(2^256), an eight-limb signed multiply-add. |tensor|<=2^30
    // makes every temporary fit Int64. A proved final height bound <2^255
    // makes the signed representative the EXACT integer polynomial value.
    static void Add256(uint[] to,int ti,uint[] from,int fi,int coefficient) {
        long carry=0;
        unchecked { for(int w=0;w<8;w++){
            long a=(long)from[fi+w]*coefficient+to[ti+w]+carry;
            to[ti+w]=(uint)a; carry=a>>32;
        }}
    }
    static string Signed256(uint[] a,int start,int sign) {
        byte[] bytes=new byte[32];
        for(int i=0;i<8;i++)Buffer.BlockCopy(BitConverter.GetBytes(a[start+i]),0,bytes,4*i,4);
        return (new BigInteger(bytes)*sign).ToString();
    }
    public static int Main(string[] args) {
        var sw=Stopwatch.StartNew();
        try {
            var ser=new JavaScriptSerializer();ser.MaxJsonLength=16000000;
            var q=ser.Deserialize<Dictionary<string,object>>(File.ReadAllText(args[0]));
            int h=Convert.ToInt32(q["h"]), batch=Convert.ToInt32(q["batch"]);
            int[] c1=Ints(q["C1"]),c2=Ints(q["C2"]),order=Ints(q["order"]);
            int[][] pairs=Rows(q["two"]), tensors=Rows(q["tensors"]);
            string mode=(string)q["mode"]; bool exact=mode=="integer256";
            long prime=Convert.ToInt64(q["prime"]);
            if(h<1||h>9||batch<1||batch>96||(!exact&&mode!="modular"))throw new Exception("backend bounds");
            if(!exact&&(prime<3||prime>2147483647))throw new Exception("prime outside Int64 product bound");
            int[][] masks=new int[h+1][]; int[] rank=new int[1<<h];
            for(int k=0;k<=h;k++){
                masks[k]=Enumerable.Range(0,1<<h).Where(m=>Pop(m)==k).ToArray();
                for(int i=0;i<masks[k].Length;i++)rank[masks[k][i]]=i;
            }
            uint[] oldZ=exact?new uint[batch*8]:null;
            long[] oldP=exact?null:new long[batch];
            for(int b=0;b<batch;b++){if(exact)oldZ[b*8]=1;else oldP[b]=1;}
            var done=new HashSet<int>();int k1=0,k2=0;long transitions=0,peakCells=batch;
            var statistics=new List<object>();
            for(int step=0;step<order.Length;step++){
                int letter=order[step]; bool in1=c1.Contains(letter),in2=c2.Contains(letter);
                int[] before=Enumerable.Range(0,pairs.Length).Where(e=>done.Contains(pairs[e][0])!=done.Contains(pairs[e][1])).ToArray();
                int[] incident=Enumerable.Range(0,pairs.Length).Where(e=>pairs[e].Contains(letter)).ToArray();
                int[] opening=incident.Where(e=>!done.Contains(pairs[e][0])&&!done.Contains(pairs[e][1])).ToArray();
                done.Add(letter);
                int[] after=Enumerable.Range(0,pairs.Length).Where(e=>done.Contains(pairs[e][0])!=done.Contains(pairs[e][1])).ToArray();
                int n1=k1+(in1?1:0),n2=k2+(in2?1:0);
                long cells=(long)Choose(h,n1)*Choose(h,n2)*(1<<after.Length)*batch;
                long oldCells=(long)Choose(h,k1)*Choose(h,k2)*(1<<before.Length)*batch;
                if((cells+oldCells)*(exact?32:8)>500000000)throw new Exception("backend live arrays exceed 500 MB");
                peakCells=Math.Max(peakCells,cells+oldCells);
                uint[] nextZ=exact?new uint[(int)cells*8]:null;
                long[] nextP=exact?null:new long[(int)cells];
                var choices=new Edge[1<<before.Length][];
                for(int oldBits=0;oldBits<choices.Length;oldBits++){
                    int global=0;for(int j=0;j<before.Length;j++)global|=((oldBits>>j)&1)<<before[j];
                    var list=new List<Edge>();
                    for(int ob=0;ob<(1<<opening.Length);ob++){
                        int g=global;for(int j=0;j<opening.Length;j++)g|=((ob>>j)&1)<<opening[j];
                        int loc=0,to=0;
                        for(int j=0;j<incident.Length;j++){int e=incident[j];int side=pairs[e][0]==letter?0:1;loc|=(((g>>e)&1)^side)<<j;}
                        for(int j=0;j<after.Length;j++)to|=((g>>after[j])&1)<<j;
                        list.Add(new Edge(loc,to,(Pop(ob)&1)==0?1:-1));
                    }choices[oldBits]=list.ToArray();
                }
                Option[][] op1=Options(masks[k1],in1,h,rank),op2=Options(masks[k2],in2,h,rank);
                int[] tensor=tensors[step];int nj=in2?h:1,nbits=1<<incident.Length;
                if(tensor.Length!=(in1?h:1)*nj*nbits*batch)throw new Exception("tensor shape mismatch");
                for(int ia=0;ia<op1.Length;ia++)for(int ib=0;ib<op2.Length;ib++)for(int bits=0;bits<choices.Length;bits++){
                    int from=((ia*op2.Length+ib)*choices.Length+bits)*batch;
                    foreach(Edge edge in choices[bits])foreach(Option i in op1[ia])foreach(Option j in op2[ib]){
                        int to=((i.Rank*masks[n2].Length+j.Rank)*(1<<after.Length)+edge.Next)*batch;
                        int ti=((i.Row*nj+j.Row)*nbits+edge.Local)*batch;
                        int sign=edge.Sign*i.Sign*j.Sign;transitions++;
                        if(exact){
                            for(int b=0;b<batch;b++){int coef=tensor[ti+b]*sign;if(coef!=0)Add256(nextZ,(to+b)*8,oldZ,(from+b)*8,coef);}
                        }else{
                            for(int b=0;b<batch;b++){
                                long t=oldP[from+b]*tensor[ti+b]%prime;
                                long v=nextP[to+b]+(sign>0?t:-t);
                                if(v<0)v+=prime;else if(v>=prime)v-=prime;nextP[to+b]=v;
                            }
                        }
                    }
                }
                oldZ=nextZ;oldP=nextP;k1=n1;k2=n2;
                statistics.Add(new{step=step,letter=letter,states=cells/batch,frontier=after.Length});
            }
            if(k1!=h||k2!=h)throw new Exception("incomplete tall columns");
            int rho=1;foreach(int[] col in new[]{c1,c2}){
                int[] positions=order.Where(col.Contains).Select(x=>Array.IndexOf(col,x)).ToArray();
                for(int i=0;i<positions.Length;i++)for(int j=i+1;j<positions.Length;j++)if(positions[i]>positions[j])rho=-rho;
            }
            string[] values=new string[batch];
            for(int b=0;b<batch;b++)values[b]=exact?Signed256(oldZ,b*8,rho):((prime+rho*oldP[b])%prime).ToString();
            var result=new{status="OK",mode=mode,values=values,transitions=transitions,
                peak_array_bytes=peakCells*(exact?32:8),seconds=sw.Elapsed.TotalSeconds,stages=statistics};
            File.WriteAllText(args[1],ser.Serialize(result));return 0;
        }catch(Exception e){Console.Error.WriteLine(e.ToString());return 1;}
    }
}

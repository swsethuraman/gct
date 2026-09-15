"""Review-only NumPy modular arithmetic; every product is reduced before summing."""
import numpy as np

def eliminate(rows,p,full=False):
    a=np.array([[int(x)%p for x in r] for r in rows],dtype=np.int64)
    nr,nc=a.shape; ids=list(range(nr)); rr=0; cs=[]; rs=[]; det=1
    for c in range(nc):
        nz=np.flatnonzero(a[rr:,c])
        if not len(nz):continue
        i=rr+int(nz[0])
        if i!=rr:a[[rr,i]]=a[[i,rr]];ids[rr],ids[i]=ids[i],ids[rr];det=-det
        pv=int(a[rr,c]);det=det*pv%p
        rs.append(ids[rr]);cs.append(c)
        a[rr,c:]=a[rr,c:]*pow(pv,-1,p)%p
        ix=np.arange(nr) if full else np.arange(rr+1,nr)
        ix=ix[ix!=rr]
        if len(ix):a[ix,c:]=(a[ix,c:] - a[ix,c,None]*a[rr,None,c:])%p
        rr+=1
        if rr==nr:break
    return rr,rs,cs,det if rr==nr==nc else 0,a

class NMod:
    def __init__(self,r,c,flat,p):self.a=np.array(flat,dtype=np.int64).reshape(r,c)%p;self.p=p
    @classmethod
    def array(cls,a,p):return cls(*a.shape,a.ravel(),p)
    def det(self):return eliminate(self.a,self.p)[3]
    def rank(self):return eliminate(self.a,self.p)[0]
    def inv(self):
        n=len(self.a);a=np.concatenate([self.a,np.eye(n,dtype=np.int64)],axis=1)
        rank,_,cs,_,red=eliminate(a,self.p,True)
        if cs!=list(range(n)):raise ValueError('singular')
        return NMod.array(red[:,n:],self.p)
    def __mul__(self,b):
        z=np.zeros((len(self.a),b.a.shape[1]),dtype=np.int64)
        for k in range(self.a.shape[1]):z=(z+self.a[:,k,None]*b.a[None,k,:])%self.p
        return NMod.array(z,self.p)
    def __getitem__(self,ij):return int(self.a[ij])

def batch_det(a,p):
    a=a.copy()%p;bn,n,_=a.shape;ix=np.arange(bn);det=np.ones(bn,dtype=np.int64)
    for k in range(n):
        nz=a[:,k:,k]!=0;good=nz.any(axis=1);row=k+nz.argmax(axis=1)
        det[~good]=0
        old=a[:,k,:].copy();a[:,k,:]=a[ix,row,:];a[ix,row,:]=old
        det=(det*np.where(row==k,1,-1))%p
        pv=a[:,k,k].copy();det=det*pv%p
        inv=np.array([pow(int(v),-1,p) if v else 1 for v in pv],dtype=np.int64)
        if k+1<n:
            fac=a[:,k+1:,k]*inv[:,None]%p
            a[:,k+1:,k+1:]=(a[:,k+1:,k+1:]-fac[:,:,None]*a[:,None,k,k+1:])%p
    return det

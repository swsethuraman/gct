"""Small exact or modular rank witnesses; no inference from deficient mod rank."""
from fractions import Fraction

def minor(A,rows,cols):return [[A[i][j] for j in cols] for i in rows]

def determinant(A,p=0):
    a=[list(row) for row in A];n=len(a)
    if any(len(row)!=n for row in a):raise ValueError('determinant requires a square matrix')
    if not n:return 1
    sign=1;previous=1
    if p:
        a=[[int(v)%p for v in row] for row in a];value=1
        for j in range(n):
            i=next((i for i in range(j,n) if a[i][j]),None)
            if i is None:return 0
            if i!=j:a[i],a[j]=a[j],a[i];sign=-sign
            pivot=a[j][j];value=value*pivot%p;inv=pow(pivot,-1,p)
            for i in range(j+1,n):
                factor=a[i][j]*inv%p
                for k in range(j+1,n):a[i][k]=(a[i][k]-factor*a[j][k])%p
        return sign*value%p
    for j in range(n-1):
        i=next((i for i in range(j,n) if a[i][j]),None)
        if i is None:return 0
        if i!=j:a[i],a[j]=a[j],a[i];sign=-sign
        pivot=a[j][j]
        for i in range(j+1,n):
            for k in range(j+1,n):
                num=a[i][k]*pivot-a[i][j]*a[j][k]
                if num%previous:raise ValueError('nonexact Bareiss division')
                a[i][k]=num//previous
            a[i][j]=0
        previous=pivot
    return sign*a[-1][-1]

def pivot_minor(A,p):
    a=[[int(x)%p for x in row] for row in A];order=list(range(len(a)));r=0;cols=[]
    for j in range(len(a[0])):
        q=next((i for i in range(r,len(a)) if a[i][j]),None)
        if q is None:continue
        a[r],a[q]=a[q],a[r];order[r],order[q]=order[q],order[r]
        inv=pow(a[r][j],-1,p)
        for i in range(r+1,len(a)):
            factor=a[i][j]*inv%p
            for k in range(j+1,len(a[0])):a[i][k]=(a[i][k]-factor*a[r][k])%p
        cols.append(j);r+=1
        if r==len(a):break
    return order[:r],cols

def rank_q(A):
    a=[[Fraction(x) for x in row] for row in A];r=0
    for j in range(len(a[0])):
        q=next((i for i in range(r,len(a)) if a[i][j]),None)
        if q is None:continue
        a[r],a[q]=a[q],a[r];pivot=a[r][j]
        for i in range(r+1,len(a)):
            factor=a[i][j]/pivot
            for k in range(j+1,len(a[0])):a[i][k]-=factor*a[r][k]
        r+=1
        if r==len(a):break
    return r

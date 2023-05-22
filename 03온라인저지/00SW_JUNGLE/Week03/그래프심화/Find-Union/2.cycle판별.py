def find(par,x):
    if par[x]!=x:
        par[x]=find(par,par[x])
    return par[x]

def union(par,a,b):
    a=find(par,a)
    b=find(par,b)
    if a<b:
        par[b]=a
    else:
        par[a]=b

v,e=map

par=[0]*(v+1)
for i in range(1,v+1):
    par[i]=i

cycle=False
for _ in range(e):
    a,b=map(int,input().split())
    if find(par,a)==find(par,b):
        cycle=True
        break
    else:
        union(par,a,b)
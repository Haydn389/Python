import sys
input=sys.stdin.readline

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

v,e=map(int,input().split())
par=[0]*(v+1)

# par=[ i for i in range()]
for i in range(1,v+1):
    par[i]=i

edges=[list(map(int,input().split())) for _ in range(e)]

edges.sort(key=lambda x:x[2])
res=0
for a,b,cost in edges:
    if find(par,a)!=find(par,b):
        union(par,a,b)
        res+=cost

print(res)
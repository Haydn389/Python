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

for i in range(1,v+1):
    par[i]=i
edges=[]
# deges=[list(map(int,input().split())) for _ in range(e)]
for _ in range(e):
    a,b,cost=map(int,input().split())
    edges.append((a,b,cost))

edges.sort(key=lambda x:x[2])
# print(edges)

res=0
for a,b,cost in edges:
    if find(par,a)!=find(par,b):
        union(par,a,b)
        res+=cost
print(res)
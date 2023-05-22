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

for i in range(e):
    a,b=map(int,input().split())
    union(par,a,b)
print(par)

for i in range(1,v+1):
    if par[i]!=i:
        find(par,i)

print(par)


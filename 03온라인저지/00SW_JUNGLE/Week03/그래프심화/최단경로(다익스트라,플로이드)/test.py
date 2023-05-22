

def find(par,x):
    if par[x]!=x:
        par=find(par,par[x])
    return par[x]
    #     return find(par,par[x])
    # return x


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

for _ in range(e):
    a,b=map(int,input().split())
    union(par,a,b)
print(par)


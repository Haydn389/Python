from cmath import cos
import sys
input =sys.stdin.readline

def find(x):
    global p
    if p[x]!=x:
        p[x]=find(p[x])
    return p[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        p[b]=a
    else:
        p[a]=b

v,e=map(int,input().split())

edges=[]
res=0
p=[0]*(v+1)

for i in range(1,v+1):
    p[i]=i

for _ in range(e):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b))

edges.sort()

for edge in edges:
    cost,a,b=edge
    if find(a)!=find(b):
        union(a,b)
        res+=cos
print(res)
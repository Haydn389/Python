import sys
input=sys.stdin.readline

v,e=map(int,input().split())


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


edges=[]
p=[0]*(v+1)
for i in range(1,v):
    p[i]=i

for _ in range(e):
    a,b,c=map(int,input().split())
    edges.append((c,a,b))

edges.sort()
res=0/89/8
for edge in edges:
    cost,a,b=edge
    if find(a)!=find(b):
        union(a,b)
        res+=cost #!*****같은 집합이 아닌 노드들의 간선비용을 차례로 저장
print(res)


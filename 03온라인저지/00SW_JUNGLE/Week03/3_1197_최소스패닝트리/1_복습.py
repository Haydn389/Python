import sys
input=sys.stdin.readline

#1) find
def find(x):
    global p
    if p[x]!=x:
        p[x]=find(p[x])
    return p[x]

#2) union
def union(a,b):
    global p
    a=find(a)
    b=find(b)
    if a<b:
        p[b]=a
    else:
        p[a]=b

#3) 노드,간선 입력받기
v,e=map(int,input().split())
#4) 노드 수 만큼 p 초기화
p=[*range(v+1)]
edges=[]
res=0

#5) 노드, 비용입력받기

for _ in range(e):
    a,b,cost=map(int,input().split())
    edges.append((a,b,cost)) #비용을 기준으로 오름차순 정렬
edges.sort(key=lambda x:x[2])

for edge in edges:
    a,b,cost=edge
    if find(a)!=find(b):
        union(a,b)
        res+=cost
print(res)
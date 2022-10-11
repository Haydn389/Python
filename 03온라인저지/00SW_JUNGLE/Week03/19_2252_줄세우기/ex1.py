import sys
from collections import deque
input=sys.stdin.readline
#노드 간선 수
v,e=map(int,input().split())

degree=[0]*(v+1)
#그래프
graph=[[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b]+=1

q=deque()

for i in range(1,1+v):
    if degree[i]==0:
        q.append(i)
res=[]
while q:
    now=q.popleft()
    res.append(now)
    for i in graph[now]:
        degree[i]-=1
        if degree[i]==0:
            q.append(i)

print(*res)
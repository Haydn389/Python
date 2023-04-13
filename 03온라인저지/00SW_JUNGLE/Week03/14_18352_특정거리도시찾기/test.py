import sys
from collections import deque

input=sys.stdin.readline

v,e,k,start=map(int,input().split())
graph=[[] for _ in range(v+1)]

for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)

def bfs(start):
    q=deque([start])
    while q:
        v=q.popleft()
        for i in graph[v]:
            # if visited[i]==0 and i!=start:
            if visited[i]==0:
                visited[i]=visited[v]+1
                q.append(i)

visited=[0]*(v+1)
visited[start]=-1
bfs(start)
for x in range(v+1):
    if visited[x] == k:
        print(x)
print(visited)
if k not in visited:
    print(-1)
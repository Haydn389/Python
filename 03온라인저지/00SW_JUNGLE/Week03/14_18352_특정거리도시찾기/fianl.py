import sys
input=sys.stdin.readline
from collections import deque


v,e,k,x= map(int, input().split())
graph=[[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
visited = [-1]*(v+1)


def bfs(x):
    q=deque([x])
    visited[x]=0
    while q:
        v=q.popleft()
        for i in graph[v]:
            if visited[i]==-1:
                visited[i]=visited[v]+1
                q.append(i)

bfs(x)
print(visited)



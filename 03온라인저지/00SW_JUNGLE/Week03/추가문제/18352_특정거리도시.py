import sys
from collections import deque
input=sys.stdin.readline
def bfs(start):
    q=deque([start])
    visited[start]=0
    while q:
        v=q.popleft()
        for i in graph[v]:
            if visited[i]==-1:
                q.append(i)
                visited[i]=visited[v]+1

v,e,k,start=map(int,input().split())

graph=[[] for _ in range(v+1)]
visited=[-1]*(v+1)

for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
bfs(start)
print(visited)
if k not in visited:
    print(-1)
else:
    for i in range(1,len(visited)):
        if visited[i]==k:
            print(i)
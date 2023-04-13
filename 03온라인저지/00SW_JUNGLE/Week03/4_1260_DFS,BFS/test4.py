import sys
sys.setrecursionlimit(10**9)
from collections import deque
input=sys.stdin.readline

v,e,start=map(int,input().split())
graph=[[] for _ in range(v+1)]
for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def dfs(v):
    visited[v]=True
    print(v,end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
    pass
def bfs(start):
    q=deque([start])
    visited[start]=True
    while q:
        v=q.popleft()
        print(v,end=" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i]=True
                q.append(i)

visited=[False]*(v+1)
dfs(start)
print()
visited=[False]*(v+1)
bfs(start)


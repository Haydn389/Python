import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
from collections import deque

v,e=map(int,input().split())
graph=[[] for _ in range(v+1)]
for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    q=deque([start])
    visited[start]=True
    while q:
        v=q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i]=True
                q.append(i)

# print(graph)
visited=[False]*(v+1)
cnt=0
for start in range(1,v+1):
    if not visited[start]:
        # bfs(start)
        dfs(start)
        cnt+=1
print(cnt)
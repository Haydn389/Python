import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
from collections import deque

v=int(input())
e=int(input())
graph=[[] for _ in range(v+1)]
for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    global cnt
    visited[v]=True
    cnt+=1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    global cnt
    q=deque([start])
    visited[start]=True
    while q:
        v=q.popleft()
        cnt+=1
        for i in graph[v]:
            if not visited[i]:
                visited[i]=True
                q.append(i)

# print(graph)
visited=[False]*(v+1)
cnt=0
bfs(1)
print(cnt)
cnt=0
visited=[False]*(v+1)
dfs(1)
print(cnt)
import sys
from collections import deque
sys.setrecursionlimit(10**5)
input=sys.stdin.readline

#노드 간선 수
v,e=map(int,input().split())
visited = [False]*(v+1)
graph=[[] for _ in range(v+1)]

def dfs(v):
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    visited[start]=True
    q=deque([start])
    while q:
        v=q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i]=True
                q.append(i)

#간선정보
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt=0
for start in range(1,v+1):
    if not visited[start]:
        bfs(start)
        cnt+=1

print(cnt)
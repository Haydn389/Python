import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)
from collections import deque
v,e,start=map(int,input().split())
graph=[[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def dfs(v):
    visited[v]=True #재귀 호출시 방문처리
    print(v,end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    q=deque([start])
    visited[start]=True
    while q:
        v=q.popleft()
        print(v,end=" ")
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i]=True #큐에 넣을 때 방문처리
    # while q:
    #     pass
    # pass


visited = [False]*(v+1)
dfs(start)
print()
visited = [False]*(v+1)
bfs(start)
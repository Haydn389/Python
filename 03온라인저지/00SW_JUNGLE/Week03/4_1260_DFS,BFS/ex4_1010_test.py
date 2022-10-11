import sys
input=sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**9)

def dfs(v):
    visited[v]=True
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
            if not visited[i]:  #***틀림! 큐에 push하는 조건 반드시 달아주기!!
                q.append(i)
                visited[i]=True

v,e,start=map(int,input().split())
graph=[[] for _ in range(v+1)]

for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited=[False]*(v+1)
dfs(start)
print()
visited=[False]*(v+1)
bfs(start)
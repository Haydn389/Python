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


def dfs(v):
    print(v,end=" ")
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    q=deque([start])
    visited[start]=True
    while q:
        v=  q.popleft()
        print(v,end=" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i]=True
                q.append(i)

def dfs2(start):
    stack=[start]
    while stack:
        v=stack.pop()
        if not visited[v]:
            print(v,end=" ")
            visited[v]=True
            for i in graph[v]:
                stack.append(i)


# visited=[False]*(v+1)
# dfs(start)
# print()
for i in graph:
    i.sort(reverse=True)
# print(graph)
visited=[False]*(v+1)
dfs2(start)
for i in graph:
    i.sort()
print()
# print(graph)
visited=[False]*(v+1)
bfs(start)
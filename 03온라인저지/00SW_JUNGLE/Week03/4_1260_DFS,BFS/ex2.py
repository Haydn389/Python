import sys
input=sys.stdin.readline
from collections import deque


def dfs(v):
    global graph,visited
    visited[v]=True
    print(v,end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    global graph,visited
    queue=deque([start])
    # queue.append(start)
    visited[start]=True

    while queue:
        v=queue.popleft()
        print(v,end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
    



if __name__=="__main__":
    v,e,start=map(int,input().split())
    graph=[[] for _ in range(v+1)]
    # graph={i:[] for i in range(v+1)}
    for _ in range(e):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(v+1):
        graph[i].sort()

    visited=[False]*(v+1)
    # print(graph)
    dfs(start)
    print()
    visited=[False]*(v+1)
    # print(graph)
    bfs(start)
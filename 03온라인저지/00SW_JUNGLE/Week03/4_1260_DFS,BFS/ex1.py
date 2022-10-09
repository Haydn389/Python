import sys
from collections import deque
input=sys.stdin.readline
def dfs(graph,v,visited):
    visited[v]=True     #재귀에 접근할 때 방문처리 및 출력
    print(v,end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)


def bfs(graph,start,visited):
    queue=deque([start]) #큐에 들어갈때 방문처리
    visited[start]=True

    while queue:
        v=queue.popleft()
        print(v,end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True


v,e,start=map(int,input().split())

graph=[[]*(v+1) for _ in range(v+1)]
# graph={ i:[] for i in range(v+1)}
for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(v+1):
    graph[i].sort()

visited=[False]*(v+1)
# print(graph)
# print(visited)
dfs(graph,start,visited)
print()
visited=[False]*(v+1)
# print(graph)
# print(visited)
bfs(graph,start,visited)
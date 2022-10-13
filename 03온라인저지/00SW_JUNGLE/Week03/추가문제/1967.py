import sys
input=sys.stdin.readline
from collections import deque


v=int(input())
graph=[[] for _ in range(v+1)]
for _ in range(v-1):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

print(graph)

visited=[0]*(v+1)
def bfs(start,cost):
    q=deque()
    q.append((start,cost))
    visited[start]=cost
    print(q)
    while q:
        v,cost=q.popleft()
        for i in graph[v]:
            if visited[i[0]]==0:
                visited[i[0]]=i[1]+cost
                q.append((i[0],i[1]))
                print(q)


bfs(1,0)
print(visited)
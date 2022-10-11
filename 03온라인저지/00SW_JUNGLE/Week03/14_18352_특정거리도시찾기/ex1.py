from collections import deque
import sys
input = sys.stdin.readline
v, e, k, x = map(int, input().split())

visited = [-1]*(v+1)

graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(start):
    q = deque([start])
    visited[start] = 0
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == -1:
                visited[i] = visited[v]+1
                q.append(i)

bfs(x)
print(visited)

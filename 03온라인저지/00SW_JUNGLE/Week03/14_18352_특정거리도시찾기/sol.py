from collections import deque
import sys
input = sys.stdin.readline
v, e, k, x = map(int, input().split())

graph = [[] for _ in range(v+1)]
distance = [-1]*(v+1)
distance[x] = 0
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)

queue = deque([x])
while queue:
    now = queue.popleft()
    for i in graph[now]:
        if distance[i] == -1:
            queue.append(i)
            distance[i] = distance[now]+1
check = True
for i in range(1, v+1):
    if distance[i] == k:
        print(i)
        check = False
if check:
    print(-1)

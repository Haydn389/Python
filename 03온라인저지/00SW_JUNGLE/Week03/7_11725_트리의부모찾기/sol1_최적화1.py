import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            parent[i]=v
            dfs(i)

v = int(input())
# parent = {i: [] for i in range(1, v+1)}

parent = [[] for _ in range(v+1)]
graph = [[] for _ in range(v+1)]
for _ in range(v-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False]*(v+1)
dfs(1)
for i in parent[2:]:
    print(i)

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(v):
    # parent[temp] = v
    visited[v] = True
    # print(v, end="")
    for i in graph[v]:
        if not visited[i]:
            # print(v)
            parent[i]=v
            dfs(i)

v = int(input())
parent = {i: [] for i in range(1, v+1)}
graph = [[] for _ in range(v+1)]
# graph={i:[] for i in range(1,v+1)}
for _ in range(v-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(v+1):
    graph[i].sort()
# print(graph)

visited = [False]*(v+1)
dfs(1)
for i in range(2,v+1):
    print(parent[i])

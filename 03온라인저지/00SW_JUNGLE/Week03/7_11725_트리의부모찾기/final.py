import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)

v=int(input())
visited = [False]*(v+1)
par = [0]*(v+1)

graph=[[] for _ in range(v+1)]

def dfs(v):
    visited[v]=True
    # print(v,end=" ")
    for i in graph[v]:
        if not visited[i]:
            par[i]=v
            dfs(i)


for _ in range(v-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
# print(par)
for p in par[2:]:
    print(p)
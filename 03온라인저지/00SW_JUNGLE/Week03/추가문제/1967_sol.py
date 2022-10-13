import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)
from collections import deque

v=int(input())
graph=[[] for _ in range(v+1)]
for _ in range(v-1):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dfs(v,cost):
    global tot,max_dist,node
    dist[v]=1
    tot+=cost
    for i in graph[v]:
        if dist[i[0]]==0:
            tot=dfs(i[0],i[1])
            if max_dist<tot:
                max_dist=tot
                node=i[0]
            tot-=i[1]
    return tot

dist=[0]*(v+1)
tot=0
node=1
max_dist=0
dfs(1,0)

dist=[0]*(v+1)
tot=0
max_dist=0
dfs(node,0)
print(max_dist)
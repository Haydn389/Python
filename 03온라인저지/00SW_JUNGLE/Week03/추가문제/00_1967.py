from collections import deque
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)

v=int(input())

graph=[[] for _ in range(v+1)]
for _ in range(v-1):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


def dfs(v,cost):
    global max_dist,node
    visited[v]=True
    print(v,cost)
    if max_dist<cost:
        max_dist=cost
        node=v
    for i in graph[v]:
        j,new_cost=i
        if not visited[j]:
            dfs(j,cost+new_cost)

def bfs(v,cost):
    global max_dist,node
    q=deque()
    q.append((v,cost))
    visited[v]=True
    while q:
        v,cost=q.popleft()
        print(v,cost)
        if max_dist<cost:
            max_dist=cost
            node=v
        for i in graph[v]:
            if not visited[i[0]]:
                visited[v]=True
                q.append((i[0],cost+i[1]))

max_dist=0
visited=[False]*(v+1)
node=1
bfs(node,0)
print(">>",node,max_dist)

max_dist=0
visited=[False]*(v+1)
bfs(node,0)
print(">>",node,max_dist)




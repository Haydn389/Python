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
    print(v,cost)
    for next,new_cost in graph[v]:
        if visited[next]==-1:
            visited[next]=cost+new_cost
            dfs(next,cost+new_cost)

def bfs(v,cost):
    global max_dist,node
    q=deque()
    q.append((v,cost))
    visited[v]=True
    while q:
        v,cost=q.popleft()
        # print(v,cost)
        if max_dist<cost:
            max_dist=cost
            node=v
        for i in graph[v]:
            if not visited[i[0]]:
                visited[v]=True
                q.append((i[0],cost+i[1]))

max_dist=0
visited=[-1]*(v+1)
dfs(1,0)
max_dist=max(visited)
node=visited.index(max_dist)
print(node,max_dist)
# print(">>",node,max_dist)

# max_dist=0
# visited=[-1]*(v+1)
# dfs(node,0)
# print(">>",node,max_dist)




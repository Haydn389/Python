import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)
v=int(input())

graph=[[] for _ in range(v+1)]
for _ in range(v-1):
    a, b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dfs(v,cost):
    global node, max_dist,tot
    visited[v]=True
    print(v,":",cost)
    tot+=cost
    for i in graph[v]:
        if not visited[i[0]]:
            # visited[i[0]]=True #!**방문처리 위에서함
            tot=dfs(i[0],i[1])
            if max_dist<tot:
                max_dist=tot
                node=i[0]
            tot-=i[1] #!***index주의
    return tot
max_dist=0
tot=0
node=1
visited = [False]*(v+1)
dfs(node,0)
print(node,max_dist)

tot=0
max_dist=0
visited = [False]*(v+1)
dfs(node,0)
print(node,max_dist)

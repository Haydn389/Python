import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

v=int(input())
graph=[[] for _ in range(v+1)]
for _ in range(v-1):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def dfs(v):
    global pos,ans
    visited[v]=True
    # print(v,end=" ")
    for i in graph[v]:
        if not visited[i]:
            ans[i]=v
            dfs(i)

visited=[False]*(v+1)
pos=2
ans=[0]*(v+1)
dfs(1,0)  
# print(ans)
for i in ans[2:]:
    print(i)
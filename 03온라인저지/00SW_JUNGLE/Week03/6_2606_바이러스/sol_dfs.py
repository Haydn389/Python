import sys
input=sys.stdin.readline
def dfs(v):
    global cnt
    visited[v]=True
    cnt+=1
    # print(v,end="")
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

v=int(input())
e=int(input())

graph=[[] for _ in range(v+1)]
# graph={i:[] for i in range(1,v+1)}
for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(v+1):
    graph[i].sort()
# print(graph)

visited=[False]*(v+1)
cnt=0
dfs(1)
# print()
print(cnt-1)
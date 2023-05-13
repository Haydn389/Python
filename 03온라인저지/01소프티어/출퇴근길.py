import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

v,e=map(int,input().split())
graph=[[] for _ in range(v+1)]
graphR=[[] for _ in range(v+1)]
for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
    graphR[b].append(a)


begin,end=map(int,input().split())
def dfs(start,visited,graph):
    # print(start)
    visited[start]=1
    for i in graph[start]:
        if not visited[i]:
            dfs(i,visited,graph)
    return

visited1=[0]*(v+1)
visited1[end]=1
dfs(begin,visited1,graph)
# print("------")
visited2=[0]*(v+1)
visited2[begin]=1
dfs(end,visited2,graph)

visited3=[0]*(v+1)
# visited3[end]=1
dfs(begin,visited3,graphR)
# print("------")
visited4=[0]*(v+1)
# visited4[begin]=1
dfs(end,visited4,graphR)
cnt=0
for i in range(1,v+1):
    if visited1[i]*visited2[i]*visited3[i]*visited4[i]==1:
        cnt+=1
print(cnt-2)
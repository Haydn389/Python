import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

v=int(input())
location=[0]+list(map(int,list(input().rstrip())))
graph=[[] for _ in range(v+1)]
ans=0
for _ in range(v-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    if location[a]==1 and location[b]==1:
        ans+=2

def dfs(v,cnt):
    visited[v]=True
    for i in graph[v]:
        if location[i]==1:
            cnt+=1
        elif not visited[i]:
            cnt=dfs(i,cnt)
    return cnt


visited = [False]*(v+1)

for start in range(1,v+1):
    if not visited[start] and location[start]==0:
        temp=dfs(start,0)
        ans+=temp*(temp-1)
print(ans)
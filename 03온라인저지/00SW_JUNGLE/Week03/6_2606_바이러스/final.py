import sys
from collections import deque
sys.setrecursionlimit(10**5)
input=sys.stdin.readline

v=int(input())
e=int(input())


#그래프
graph=[[] for _ in range(v+1)]

#간선정보
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v,cnt):
    visited[v]=True
    cnt+=1
    for i in graph[v]:
        if not visited[i]:
            cnt=dfs(i,cnt)
    return cnt

def bfs(v):
    global ans
    visited[v]=True
    q=deque([v])
    while q:
        v=q.popleft()
        for i in graph[v]:
            if not visited[i]:
                ans+=1
                visited[i]=True
                q.append(i) 

visited = [False]*(v+1)
print(dfs(1,0)-1)
# visited = [False]*(v+1)
# ans=0
# bfs(1)
# print(ans)
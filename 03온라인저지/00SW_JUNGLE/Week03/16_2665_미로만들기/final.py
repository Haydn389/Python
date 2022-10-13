#다익스트라
import heapq
import sys
input=sys.stdin.readline
from heapq import heappop,heappush
INF=int(1e9)
n=int(input())
a = [list(map(int,list(input().rstrip()))) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]

q=[]
cnt=0
heappush(q,(cnt,0,0))
visited[0][0]=True
#검은 방을 
while q:
    cnt,x,y=heappop(q)
    if x==n-1 and y==n-1:
        print(cnt)
        break
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i] 
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
            visited[nx][ny]=True
            if a[nx][ny]==1:
                heappush(q,(cnt,nx,ny))
            elif a[nx][ny]==0:
                a[nx][ny]=1
                heappush(q,(cnt+1,nx,ny))

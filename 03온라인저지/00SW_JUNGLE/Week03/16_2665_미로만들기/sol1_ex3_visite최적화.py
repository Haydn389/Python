from heapq import heapify,heappop,heappush
import sys
input=sys.stdin.readline
n=int(input())
a=[list(map(int,input().rstrip())) for _ in range(n)]
visited=[[0]*n for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    q=[]
    cnt=0
    heappush(q,[cnt,x,y])
    a[x][y]=2
    while q:
        cnt,x,y=heappop(q)
        if x==n-1 and y==n-1:
            print(cnt)  #!*** cnt를 꺼냈으므로 바로 print
            return
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and a[nx][ny]!=2:  #!***x,y가 아니라 ny,ny임
                a[nx][ny]=2 
                if a[nx][ny]==0:
                    heappush(q,[cnt+1,nx,ny])
                else:
                    heappush(q,[cnt,nx,ny])



bfs(0,0)
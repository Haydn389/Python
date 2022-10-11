import sys
from heapq import heapify,heappop,heappush
input=sys.stdin.readline

n=int(input())

a=[list(map(int,input().rstrip())) for _ in range(n)]
visited=[[0]*n for _ in range(n)]


def ds(x,y):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    h=[]
    heappush(h,[0,x,y]) #벽을 부순횟수, x,y
    visited[x][y]=True

    while h:
        cnt,x,y=heappop(h)
        if x==n-1 and y==n-1:
            print(cnt)
            return
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==False:
                visited[nx][ny]=True
                if a[nx][ny]==0: #검은방이면 변경횟수 count하여 넘겨주기
                    heappush(h,[cnt+1,nx,ny])
                elif a[nx][ny]==1: #흰방이면 동일하게 저장
                    heappush(h,[cnt,nx,ny])
        # print("*"*50)
        # print(h)
        # for p in visited:
        #     for o in p:
        #         print("{:>3}".format(o),end="")
        #     print()


ds(0,0)
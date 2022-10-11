from heapq import heapify,heappop,heappush
n=int(input())
a=[list(map(int,list(input().rstrip()))) for _ in range(n)]
visited=[[False]*n for _ in range(n)]
# print(a)
dx=[1,-1,0,0]
dy=[0,0,1,-1]

def ds(x,y):
    q=[]
    cnt=0
    heappush(q,[cnt,x,y]) #벽 부순횟수, x,y좌표
    visited[0][0]=True
    while q:
        cnt,x,y=heappop(q)
        if x==n-1 and y==n-1:
            print(cnt)
            return
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]: #!*** nx,ny 혼용주의
                visited[nx][ny]=True                
                if a[nx][ny]==1:
                    heappush(q,[cnt,nx,ny])
                elif a[nx][ny]==0:              #!** 사실 그냥 else로 해도됨
                    heappush(q,[cnt+1,nx,ny])


ds(0,0)
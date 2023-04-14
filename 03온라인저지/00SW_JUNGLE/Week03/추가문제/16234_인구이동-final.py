import sys
from collections import deque
input=sys.stdin.readline
n,l,r=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    global a,flag
    open=[]
    temp=0
    tot=0
    visited[x][y]=1
    q=deque([(x,y)])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0 and l<=abs(a[x][y]-a[nx][ny])<=r:
                flag=False
                if not open:
                    open.append((x,y))
                    tot+=a[x][y]
                open.append((nx,ny))
                tot+=a[nx][ny]
                q.append((nx,ny))
                visited[nx][ny]=2
                temp+=1
    if open:
        avg=tot//len(open)
        for x,y in open:
            a[x][y]=avg
cnt=0
flag=True
while True:
    visited=[[0]*n for _ in range(n)]
    flag=True
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i,j)
    if flag==True:
        print(cnt)
        break
    cnt+=1
import sys
input=sys.stdin.readline
from collections import deque

n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
S,X,Y=map(int,input().split())

virus=[]
for i in range(n):
    for j in range(n):
        if a[i][j]!=0:
            virus.append((a[i][j],i,j,0))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
virus.sort()

q=deque(virus)

while q:
    v,x,y,cnt=q.popleft()
    if cnt==S:
        break
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<n and a[nx][ny]==0:
            a[nx][ny]=a[x][y]
            q.append((v,nx,ny,cnt+1))
    # print(">>>cnt",cnt)
    # for p in a:
    #     print(p)
    # print("-"*30)

print(a[X-1][Y-1])


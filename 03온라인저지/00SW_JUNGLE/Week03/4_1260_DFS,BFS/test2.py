import sys
input=sys.stdin.readline
from collections import deque
v=int(input())
a=[list(map(int,input().rstrip())) for _ in range(v)]

def bfs(x,y):
    q=deque((x,y))
    a[x][y]=2
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<v and 0<=ny<v and a[nx][ny]==1:
                a[nx][ny]=2
                q.append((nx,ny))
cnt=0
res=[]
for i in range(v):
    for j in range(v):
        if a[i][j]==1:
            temp=bfs(i,j)
            res.append(temp)

import sys
input=sys.stdin.readline
from collections import deque
n,m=map(int,input().split())
a=[list(map(int,list(input().rstrip()))) for _ in range(n)]
dx=[1,-1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if a[nx][ny]!=1:
                continue
            if a[nx][ny]==1:
                a[nx][ny]=a[x][y]+1
                q.append((nx,ny))
    return a[n-1][m-1]

print(bfs(0,0))

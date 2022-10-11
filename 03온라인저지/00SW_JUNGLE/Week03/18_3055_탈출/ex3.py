from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split())

a=[list(input().rstrip()) for _ in range(n)]
visited=[[0]*m for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(Dx,Dy):
    while q:
        x,y=q.popleft()
        if a[Dx][Dy]=="S":
            return visited[Dx][Dy]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if a[x][y]=="S" and (a[nx][ny]=="." or a[nx][ny]=="D"):
                    visited[nx][ny]=visited[x][y]+1
                    a[nx][ny]="S"
                    q.append((nx,ny)) 
                elif a[x][y]=="*" and (a[nx][ny]=="." or a[nx][ny]=="S"):
                    a[nx][ny]="*"
                    q.append((nx,ny)) 
    return "KAKTUS"
q=deque()

for i in range(n):
    for j in range(m):
        if a[i][j]=="S":
            q.append((i,j))
        elif a[i][j]=="D":
            Dx,Dy=i,j

for i in range(n):
    for j in range(m):
        if a[i][j]=="*":
            q.append((i,j))

print(bfs(Dx,Dy))
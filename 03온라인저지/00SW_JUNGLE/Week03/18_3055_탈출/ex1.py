#고슴도치의 위치 큐에 삽입
#굴위치 저장
#물 위치 q에 저장

from collections import deque
import re
import sys
input=sys.stdin.readline
n,m=map(int,input().split())

a=[list(input().rstrip()) for _ in range(n)]
visited=[[0]*m for _ in range(n)]
q=deque()
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
            #범위 내에 있다면
            if 0<=nx<n and 0<=ny<m:                     #!***not visied 필요x 
                if a[x][y]=="S" and (a[nx][ny]=="." or a[nx][ny]=="D"):
                    a[nx][ny]="S"                       #!*** "S" 고슴도치 이동시키기
                    visited[nx][ny]= visited[x][y]+1    #!***이동횟수는 visited에 저장
                    q.append((nx,ny))                   #!***고슴도치의 좌표는 q에 push
                elif a[x][y]=="*" and (a[nx][ny]=="." or a[nx][ny]=="S"):
                    a[nx][ny]="*"                       #!*** '*'이동
                    q.append((nx,ny))
    return "KAKTUS"
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
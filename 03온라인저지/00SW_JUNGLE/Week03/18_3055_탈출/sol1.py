#https://wookcode.tistory.com/167
from collections import deque
n,m=map(int,input().split())

a=[list(input().rstrip()) for _ in range(n)]
visited=[[0]*m for _ in range(n)]
dx,dy=[-1,1,0,0],[0,0,-1,1]

q=deque()


# print(q)
dx,dy=[1,-1,0,0],[0,0,1,-1]
def bfs(Dx,Dy):
    while q:
        x,y=q.popleft()
        if a[Dx][Dy]=="S": #굴에 S가 도달했을때
            return visited[Dx][Dy]
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i] 
            if 0<=nx<n and 0<=ny<m: #그래프 범위 내에있고
                #꺼낸 노드가 고슴도치 이고 인접노드가 . or "D"일때
                if a[x][y]=="S" and(a[nx][ny]=="." or a[nx][ny]=='D'):
                    a[nx][ny]="S"
                    visited[nx][ny]=visited[x][y]+1 #!**
                    q.append((nx,ny))
                #R꺼낸 노드가 물이고 인접노드가 . or "S"일때
                elif a[x][y]=="*" and(a[nx][ny]=="." or a[nx][ny]=="S"):
                    a[nx][ny]="*"
                    q.append((nx,ny))
    #while문 안에서 return 되지 않았으면 
    return "KAKTUS"

for i in range(n):
    for j in range(m):
        if a[i][j]=='S':
            q.append((i,j))
        elif a[i][j]=='D':
            Dx,Dy=i,j


for i in range(n):
    for j in range(m):
        if a[i][j]=="*":
            q.append((i,j))

print(bfs(Dx,Dy))
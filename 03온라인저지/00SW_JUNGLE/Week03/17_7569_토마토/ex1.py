from collections import deque
import sys
input=sys.stdin.readline

m,n,h=map(int,input().split())

a=[[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
dx=[1,-1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,1,-1]
q=deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if a[i][j][k]==1:
                q.append((i,j,k))

while q:
    x,y,z=q.popleft()
    for i in range(6):
        nx=x+dx[i]
        ny=y+dy[i]
        nz=z+dz[i]
        if 0<=nx<h and 0<=ny<n and 0<=nz<m and a[nx][ny][nz]==0:
            a[nx][ny][nz]=a[x][y][z]+1
            q.append((nx,ny,nz))

ans=0
for i in a:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        ans=max(ans,(max(j)))

print(ans-1)
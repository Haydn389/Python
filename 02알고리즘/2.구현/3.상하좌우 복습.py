import sys

n=int(sys.stdin.readline().strip())

data=list(sys.stdin.readline().split())

dir=['R','L','D','L']
dx=[0,0,1,-1]
dy=[1,-1,0,0]
x=y=1

for i in data:
    for j in range(4):
        if i==dir[j]:
            nx=x+dx[j]
            ny=y+dy[j]
    if 1<=nx<=n and 1<=ny<=n:
        x,y=nx,ny
print(x,y)

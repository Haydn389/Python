import sys
input =sys.stdin.readline

n=int(input())
a=list(input().split())

dx=[-1,1,0,0]
dy=[0,0,-1,1]
s=["U","D","L","R"]
x=y=1
for dir in a:
    move=s.index(dir)
    nx=dx[move]
    ny=dy[move]
    if 1<=x+nx<=n and 1<=y+ny<=n:
        x+=nx
        y+=ny
print(x,y)

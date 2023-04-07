import sys
input = sys.stdin.readline

n,m=map(int,input().split())
x,y,dir=map(int,input().split())
map=[list(map(int,input().split())) for _ in range(n)]
# dir=[(0,1),(-1,0),(0,-1),(1,0)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]

ans=0
map[x][y]=1
while(True):
    pre=(x,y)
    for i in range(4):
        dir-=1
        nx=x+dx[dir%4]
        ny=y+dy[dir%4]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if map[nx][ny]==0:
            map[nx][ny]=1
            x=nx
            y=ny
            ans+=1
            break

    post=(x,y)
    print('=====')
    for j in map:
        print(j)
    if pre==post:
        break
print(ans+1)
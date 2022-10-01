import sys
x,y = map(int,sys.stdin.readline().split())

dx=[0,0,1,-1]
dy=[1,-1,0,0]

for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if 0<=nx<5 and 0<=ny<5:
        print(i+1,"번째 이동")
        print('(',nx,',',ny,')')

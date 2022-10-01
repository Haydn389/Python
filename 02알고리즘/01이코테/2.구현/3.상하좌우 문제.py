import sys
n=int(sys.stdin.readline().strip())

dir = sys.stdin.readline().split()
x,y=1,1
dx=[0,0,1,-1]
dy=[1,-1,0,0]

move=['R','L','D','U']
for i in dir:
    for j in range(len(move)):
        if (i == move[j]):
            nx=x+dx[j]
            ny=y+dy[j]
        if nx<1 or ny<1 or nx > n or ny > n: #key point
            continue    #key point
        x,y=nx,ny
    print('(',x,',',y,')')


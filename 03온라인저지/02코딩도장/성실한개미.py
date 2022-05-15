import sys
n,m=10,10
data=[[]*m for _ in range(n)]
for i in range(n):
    data[i]=list(map(int,sys.stdin.readline().split())) #한 줄에 입력된 원소들을 리스트화 시켜줌

dx=[0,1]
dy=[1,0]
nx=ny=1
x=y=1


while True:
    data[x][y]=9
    if data[x][y+1]==1:
        nx=x+dx[1]
        ny=y+dy[1]
    else:
        nx=x+dx[0]
        ny=y+dy[0]

    x,y=nx,ny
    if (data[x][y]==2)or(data[x][y+1]==1 and data[x+1][y]==1):
        data[x][y]=9
        break

# print(data)
for i in range(n):
    for j in range(m):
        print(data[i][j],end=' ')
    print()
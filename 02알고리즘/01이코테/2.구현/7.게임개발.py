import sys
n,m=map(int,sys.stdin.readline().split())
x,y,d=map(int,sys.stdin.readline().split())

check=[[0]*m for _ in range(n)]
array=[]
## 북 동 남 서
dx=[-1,0,1,0]
dy=[0,1,0,-1]

for i in range(n):
    array.append(list(map(int,sys.stdin.readline().split())))


def turn_left():
    global d
    if d==0:
        d=3
    else: d-=1


check[x][y]=1
cnt=1
turn_time=0
while True:
    turn_left() #방향회전
    # print(d)
    nx=x+dx[d] #회전 후 이동할 좌표계산
    ny=y+dy[d]

    #이동할 좌표 방문이력 and 바다인지 확인
    if array[nx][ny]==0 and check[nx][ny]==0:
        check[nx][ny]=1
        x,y=nx,ny
        cnt+=1
        turn_time=0

    else: turn_time+=1

    if turn_time==4:
        nx = x-dx[d]
        ny = y - dy[d]
        if array[nx][ny]==0:
            x,y=nx,ny
        else:
            break
        turn_time=0
print(cnt)
for i in range(n):
    for j in range(m):
        print(check[i][j],end=" ")
    print()





# sum=0
# for i in range(n):
#     for j in range(m):
#         sum+=int(check[i][j])
#         print(check[i][j],end=" ")
#     print()
# print(sum)
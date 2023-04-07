import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph=[[0]*(n+1) for _ in range(n+1)]
num= int(input())
for _ in range(num):
    a,b=map(int,input().split())
    graph[a][b]=1

r_num=int(input())
rot={}
for _ in range(r_num):
    c,d=input().split()
    rot[int(c)]=d

print(n)
print(rot)
for f in graph:
    print(f)
print("-"*30)

x,y=1,1 #시작 좌표
dir=0
#우하좌상
dx=[0,1,0,-1]
dy=[1,0,-1,0]
tick=0
snake=deque()
snake.append((x,y))
while(True):
    graph[x][y]=2
    if tick in rot:
        if rot[tick] == "D":
            dir+=1
        else:
            dir-=1
    nx=x+dx[dir%4]
    ny=y+dy[dir%4]
    flag=False
    # 범위를 벗어났거나, 몸통에 부딪히면
    if 1>nx or nx>n or 1>ny or ny>n or graph[nx][ny]==2:
        tick+=1
        print(tick)
        break
    # 범위 내
    snake.append((nx,ny))
    if graph[nx][ny]==0: #사과 없다면
        tail=snake.popleft()
        print(tail)
        graph[tail[0]][tail[1]]=0 #꼬리제거
    graph[nx][ny]=2 #앞으로 전진

    x,y=nx,ny
    tick+=1
    print("tick",tick)
    print("snake :",snake)
    for p in graph:
        print(p)
    print("-"*30)
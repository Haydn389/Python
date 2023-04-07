import sys
from collections import deque
input = sys.stdin.readline

n=int(input())
graph=[[0]*(n+1) for _ in range(n+1)]
apple={}

for _ in range(int(input())):
    a,b=map(int,input().split())
    graph[a][b]=1
    # apple[a]=b

turn={}
for _ in range(int(input())):
    a,b=input().split()
    turn[int(a)]=b

#시작좌표
x,y=1,1
#뱀 저장
snake=deque()
snake.append((x,y))
tick=0
#회전순서(우,상,좌,하)
dx=[0,-1,0,1]
dy=[1,0,-1,0]
dir=0

for i in graph:
    print(i)
print("*"*30)

while(True):
    tick+=1
    #1)이동하기
    nx=x+dx[dir%4]
    ny=y+dy[dir%4]
    #2) 조건되면 탈출
    if nx<1 or nx>n or ny<1 or ny>n or graph[nx][ny]==2:
        # print(nx,ny,graph[nx][ny])
        print(tick)
        break
    #3) 아니면 뱀 위치 조정
    snake.append((nx,ny))
    if graph[nx][ny]!=1:
        graph[nx][ny]=2
        tail=snake.popleft()     
        graph[tail[0]][tail[1]]=0
    else:
        graph[nx][ny]=2
    #4) 회전 확인
    if tick in turn:
        if turn[tick]=='D':
            dir-=1
        else:
            dir+=1
    print(f">>> tick :{tick}, \n>>> snake : {snake}")
    for i in graph:
        print(i)
    print("-"*30)
    x,y=nx,ny
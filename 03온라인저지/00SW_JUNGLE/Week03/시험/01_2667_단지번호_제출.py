import sys
input=sys.stdin.readline
from collections import deque
v=int(input())
a = [list(map(int,list(input().rstrip()))) for _ in range(v)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y):
    q=deque()
    q.append((x,y))
    num=0 #집 갯수 초기화
    a[x][y]=2
    while q:
        x,y=q.popleft()
        num+=1 #pop할때 집 갯수 세기
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i] 
            if 0<=nx<v and 0<=ny<v and a[nx][ny]==1:
                a[nx][ny]=2
                q.append((nx,ny))
    return num

cnt=0 #단지 수 카운트
res=[]
for i in range(v):
    for j in range(v):
        if a[i][j]==1:
            cnt+=1
            temp=bfs(i,j)
            res.append(temp)

print(cnt) 
for p in sorted(res):
    print(p)



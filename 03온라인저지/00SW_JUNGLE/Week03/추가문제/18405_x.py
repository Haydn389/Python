import sys
from collections import deque
input=sys.stdin.readline

n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
S, X, Y=map(int, input().split())
X=X-1
Y=Y-1
virus=[]
q=deque()
for i in range(n):
    for j in range(n):
        if a[i][j]!=0:
            virus.append((a[i][j],i,j))
virus.sort()
q=deque(virus)
# print(q)
time=len(q)
dx=[0,1,0,-1]
dy=[1,0,-1,0]
def bfs():
    cnt=0
    sec=0
    while q:
        if cnt==time:
            sec+=1
            cnt=0
            if sec==S:break
        v,x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i] 
            if 0<=nx<n and 0<=ny<n and a[nx][ny]==0:
                a[nx][ny]=a[x][y]
                q.append((v,nx,ny))
        cnt+=1
        # print("*"*50)
        # print(">>>cnt",cnt)
        # for p in a:
        #     print(*p)
bfs()
# print(a)
print(a[X][Y])


import sys
from collections import deque
input=sys.stdin.readline
n=int(input())

a = [list(map(int,list(input().rstrip()))) for _ in range(n)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
def bfs(x,y):
    num=0
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i] 
            if 0<=nx<n and 0<=ny<n and a[nx][ny]==1:
                a[nx][ny]=2
                num+=1
                q.append((nx,ny))
    return num

cnt=0
res=[]
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            cnt+=1
            temp=bfs(i,j)
            if temp==0:res.append(1)
            else:res.append(temp)
            # for p in a:
            #     print(*p)
print(cnt)
for r in sorted(res):
    print(r)
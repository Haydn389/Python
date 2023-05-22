import sys
from collections import deque
sys.setrecursionlimit(10**9)

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y):
    q=deque([(x,y)])

def bfs(x,y):
    global cnt
    q=deque([(x,y)])
    a[x][y]=2
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and a[nx][ny]==1:
                q.append((nx,ny))
                a[nx][ny]=2
                cnt+=1


n=int(input())
a=[list(map(int,input().rstrip())) for _ in range(n)]
cnt=0
res=[]
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            cnt=1
            bfs(i,j)
            res.append(cnt)

print(len(res))
for r in sorted(res):
    print(r)
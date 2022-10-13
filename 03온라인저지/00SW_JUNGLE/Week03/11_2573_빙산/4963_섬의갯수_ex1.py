import sys
input=sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**5)

dx=[-1,1,0,0,1,1,-1,-1]
dy=[0,0,-1,1,1,-1,1,-1]
def dfs(x,y):
    a[x][y]=2
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i] 
        if 0<=nx<n and 0<=ny<m and a[nx][ny]==1:
            dfs(nx,ny)
            # print("-"*50)
            # for p in a:
            #     print(*p)

def bfs(x,y):
    q=deque()
    q.append((x,y))
    a[x][y]=2
    while q:
        x,y=q.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i] 
            if 0<=nx<n and 0<=ny<m and a[nx][ny]==1:
                a[nx][ny]=2
                q.append((nx,ny))
        # print("-"*50)
        # for p in a:
        #     print(*p)
while True:
    m,n = map(int, input().split())
    if m==0 and n==0: break
    a = [list(map(int, input().split())) for _ in range(n)]
    cnt=0
    for i in range(n):
        for j in range(m):
            if a[i][j]==1:
                cnt+=1
                dfs(i,j)
                # print(">>>",cnt)
    print(cnt)
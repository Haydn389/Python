import sys
from collections import deque
sys.setrecursionlimit(10**5)
input=sys.stdin.readline

n,m=map(int,input().split())
#공백없는 2차원 리스트
a = [list(map(int,list(input().rstrip()))) for _ in range(n)]
dx,dy=[-1,1,0,0],[0,0,-1,1]
# visited=[[False]*m for _ in range(n)]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    # visited[x][y]=True
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i] 
            # if 0<=nx<n and 0<=ny<m and a[nx][ny]!=0 and not visited[nx][ny]:
            if 0<=nx<n and 0<=ny<m and a[nx][ny]==1:
                # visited[nx][ny]=True
                a[nx][ny]=a[x][y]+1
                q.append((nx,ny))
    # print(a)


bfs(0,0)
print(a[n-1][m-1])
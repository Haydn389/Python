import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
a=[list(map(int,input().rstrip())) for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    q=deque([(x,y)])
    # q=deque()
    # q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i] 
            ny=y+dy[i] 
            if 0<=nx<n and 0<=ny<m and a[nx][ny]==1:
                a[nx][ny]=a[x][y]+1
                q.append((nx,ny))
        # for k in a:
        #     print(k)
        # print("="*30)
bfs(0,0)
# for g in a:
#     print(g)

print(a[n-1][m-1])
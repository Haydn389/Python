import sys
from collections import deque
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n,m=map(int,input().split())

# a=[list(map(int,list(input().rstrip()))) for _ in range(n)]
a=[]
for _ in range(n):
    a.append(list(map(int,input().rstrip())))
# print(n,m)
# print(a)
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y):
    queue=deque()
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # if x<0 or y<0 or x>=n or y>=m or a[nx][ny]!=1: #****틀림! x,y가 아니라 nx,ny임 
            if nx<0 or ny<0 or nx>=n or ny>=m or a[nx][ny]!=1: 
                continue
            if a[nx][ny]==1:
                a[nx][ny]=a[x][y]+1
                queue.append((nx,ny))

    return a[n-1][m-1]


print(bfs(0,0))
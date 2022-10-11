import sys
from collections import deque
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int,list(input().rstrip()))) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and a[nx][ny]==1: #범위를 벗어났거나 길이 아닌곳일때(1이 아닐때)
                a[nx][ny]=a[x][y]+1
                queue.append((nx,ny))
    return a[n-1][m-1]
print(bfs(0,0))


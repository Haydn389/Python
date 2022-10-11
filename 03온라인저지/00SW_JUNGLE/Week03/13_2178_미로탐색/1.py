import sys
from collections import deque
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int,list(input().rstrip()))) for _ in range(n)]
for p in a:
    print(*p)
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
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if a[nx][ny]==0:
                continue
            if a[nx][ny]==1:
                a[nx][ny]=a[x][y]+1
                queue.append((nx,ny))
        print("*"*50)
        for p in a:
            print(*p)
    return a[n-1][m-1]
print(bfs(0,0))
# cnt = 0
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == '0':
#             dfs(i, j)
#             cnt += 1


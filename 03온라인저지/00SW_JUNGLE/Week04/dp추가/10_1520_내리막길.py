import sys
input=sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

visited=[[-1]*m for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(x,y):
    if x==n-1 and y==m-1:
        return 1
    if visited[x][y]!=2:
        return visited[x][y]
    visited[x][y]=0
    print("-"*50)
    for p in visited:
        print(p)
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i] 
        if 0<=nx<n and 0<=ny<m and a[nx][ny]<a[x][y]:
            visited[nx][ny]+=dfs(nx,ny)
    return visited[x][y]
dfs(0,0)
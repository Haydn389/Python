import sys

input=sys.stdin.readline

n=int(input())

a=[list(map(int,input().split())) for _ in range(n)]
visited=[[-1]*n for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(x,y):
    print("*"*50)
    for p in visited:
        print(p)
    if x==n-1 and y==n-1:
        return 1    
    if visited[x][y]!=-1:
        return visited[x][y]
    visited[x][y]=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i] 
        if 0<=nx<n and 0<=ny<n and a[nx][ny]>a[x][y]:
            visited[x][y]+=dfs(nx,ny)
            print("-"*50)
            for p in visited:
                print(p)
    return visited[x][y]


cnt=0
dfs(1,0)

# for i in range(n):
#     for j in range(n):
#         if visited!=-1:
#             dfs(i,j)

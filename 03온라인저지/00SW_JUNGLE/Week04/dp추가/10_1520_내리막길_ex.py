import sys
sys.setrecursionlimit(10**9)


input=sys.stdin.readline
n,m=map(int,input().split())

a=[list(map(int,input().split())) for _ in range(n)]

visited=[[False]*m for _ in range(n)]
print(a)
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    print("*"*50)
    for p in visited:
        print(p)
    #방문한 적 있으면 다시 안들어감
    if visited[x][y]:
    # if visited[x][y]!=-1:
        return visited[x][y]
    #방문안한 곳이면 
    visited[x][y]=0
    if x==n-1 and y==m-1:
        return 1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and a[nx][ny]<a[x][y]:
            visited[x][y]=visited[x][y]+dfs(nx,ny)
            print("-"*50)
            for p in visited:
                print(p)
    return visited[x][y]
    # print(visited[x][y])


print(dfs(0,0))
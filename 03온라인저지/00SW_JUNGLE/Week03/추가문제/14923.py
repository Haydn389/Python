import sys,copy
from collections import deque

n,m=map(int,input().split())
x0,y0=map(int,input().split())
x1,y1=map(int,input().split())

graph_origin=[list(map(int,input().split())) for _ in range(n)]
wall=[]
for i in range(n):
    for j in range(m):
        if graph_origin[i][j]==1:
            wall.append((i,j))
print(graph_origin)
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x0,y0,x1,y1,graph):
    q=deque([(x0,y0)])
    # graph[x0][y0]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
                graph[nx][ny]=graph[x][y]+1
                q.append((nx,ny))

    print("----후-----")
    for z in graph:
        print(z)
    return graph[x1][y1]
ans=sys.maxsize

for wx,wy in wall:
    graph=copy.deepcopy(graph_origin)
    graph[wx][wy]=0
    print("=========wx,wy",wx,wy)
    print("----전-----")
    for z in graph:
        print(z)
    ans=min(ans,bfs(x0-1,y0-1,x1-1,y1-1,graph))


print(ans)


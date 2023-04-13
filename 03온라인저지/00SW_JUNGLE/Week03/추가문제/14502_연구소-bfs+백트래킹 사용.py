import sys,copy
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
from collections import deque

n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
wall=[]
virus=[]
for i in range(n):
    for j in range(m):
        if a[i][j]==0:
            wall.append((i,j))
        if a[i][j]==2:
            virus.append((i,j))

dx=[-1,1,0,0]
dy=[0,0,1,-1]
ans=0

def bfs(x0,y0,graph):
    q=deque([(x0,y0)])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
                graph[nx][ny]=2
                q.append((nx,ny))

    return graph

# graph=copy.deepcopy(a)
# bfs(1,5,graph)
def back(depth):
    global ans
    if depth==3:
        graph=copy.deepcopy(a)
        cnt=0
        for x,y in virus:
            graph=bfs(x,y,graph)

        for i in range(n):
            for j in range(m):
                if graph[i][j]==0:
                    cnt+=1
        ans = max(ans,cnt)
        return
    
    for i in range(n):
        for j in range(m):
            if a[i][j]==0:
                a[i][j]=1
                back(depth+1)
                a[i][j]=0
back(0)
print(ans)

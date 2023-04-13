#시간초과
import sys,copy
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

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
def dfs(x,y,graph):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
            graph[nx][ny]=2
            dfs(nx,ny,graph)
    return graph
ans=0

def back(depth):
    global ans
    if depth ==3:
        graph=copy.deepcopy(a)
        for x,y in virus:
            graph=dfs(x,y,graph)
        cnt=0
        for i in range(n):
            for j in range(m):
                if graph[i][j]==0:
                    cnt+=1
        ans=max(ans,cnt)
        return
    
    for i in range(n):
        for j in range(m):
            if a[i][j]==0:
                a[i][j]=1
                back(depth+1)
                a[i][j]=0
back(0)

print(ans)

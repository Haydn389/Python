import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(y,x):
    graph[y][x]=2
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if 0<=ny<n and 0<=nx<m and graph[ny][nx]==1:
            graph[ny][nx]=2
            dfs(ny,nx)


for _ in range(int(input())):
    m,n,num=map(int,input().split())#n==y, m==x
    graph=[[0]*m for _ in range(n)]

    for _ in range(num):
        x,y=map(int,input().split())
        graph[y][x]=1
    cnt=0
    for y in range(n):
        for x in range(m):
            if graph[y][x]==1:       
                dfs(y,x)
                for p in graph:
                    print(p)
                print("-"*30)
                cnt+=1
    # for p in graph:
    #     print(p)
    # print("-"*30)
    print(">>>",cnt)
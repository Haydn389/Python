import sys,copy
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
from collections import deque
from itertools import combinations

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
def dfs(x,y):
    global graph
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
            graph[nx][ny]=2
            dfs(nx,ny)
    # for p in graph:
    #     print(p)
    # print("-"*30)

ans=0
for w in combinations(wall,3):

    #개별 case1), 2)...
    graph=copy.deepcopy(a)
    #새로운 벽 위치 세우기
    # for i,j in [(0, 0), (0, 1), (0, 2)]:
    for i,j in w:
        graph[i][j]=1
    # for p in graph:
    #     print(p)
    # print("*"*30)
    #바이러스 있는 곳 부터
    for x,y in virus:
        # print(x,y)
        dfs(x,y)
    cnt=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                cnt+=1
    temp=ans
    ans=max(ans,cnt)
    # if temp !=ans:
    #     print(">>>w:",ans)

print(ans)
# print(wall)
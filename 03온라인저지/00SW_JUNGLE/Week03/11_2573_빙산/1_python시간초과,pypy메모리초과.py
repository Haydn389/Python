#https://lazypazy.tistory.com/101

import sys,copy
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

n,m=map(int,input().split())

a=[list(map(int,input().split())) for _ in range(n)]

# visited=[[False]*m for _ in range(n)]
# print(n,m)
# for i in a:print(i)
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(visited,x,y):
    if x<=0 or x>=n-1 or y<=0 or y>=m-1:
        return False
    if visited[x][y]!=0:
        visited[x][y]=0
        dfs(visited,x-1,y)
        dfs(visited,x,y-1)
        dfs(visited,x+1,y)
        dfs(visited,x,y+1)
        return True
    return False

def melt(a):
    temp=[[0]*m for _ in range(n)]
    for x in range(1,n-1):
        for y in range(1,m-1):
            water=0
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if a[nx][ny]==0:water+=1
            if a[x][y]-water<0:
                temp[x][y]=0
            else:temp[x][y]=a[x][y]-water
    return copy.deepcopy(temp)

# a=melt(a)
# visited=a[:]
# for i in a:print(*i)
# for i in visited:print(*i)


year=0
while True:
    print("*"*50)
    print("지금 year",year)
    cnt=0
    visited=copy.deepcopy(a)
    print("dfs 전")
    for i in visited:print(*i)
    for i in range(1,n-1):
        for j in range(1,m-1):
            if dfs(visited,i,j)==True:
                cnt+=1

    print("dfs 후")
    for i in visited:print(*i)
    print("이번step cnt",cnt)
    if cnt==0: break        #빙하가 다 녹으면 종료
    elif cnt!=1: break
    print("melt 전")
    for i in a:print(*i)
    a=melt(a)
    year+=1
    print("melt 후")
    for i in a:print(*i)

print(year)

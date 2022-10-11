import sys,copy
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]

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
            ice=a[x][y]-water
            temp[x][y]=ice if ice>0 else 0
            # if a[x][y]-water<0:
            #     temp[x][y]=0
            # else:temp[x][y]=a[x][y]-water
    return copy.deepcopy(temp)

year=0
while True:
    cnt=0
    visited=copy.deepcopy(a)
    for i in range(1,n-1):
        for j in range(1,m-1):
            if dfs(visited,i,j)==True:
                cnt+=1
    if cnt==0: break        #빙하가 다 녹으면 종료
    elif cnt!=1: break

    a=melt(a)
    year+=1

print(year)

import sys
from itertools import combinations
input=sys.stdin.readline

n,k=map(int,input().split())
arr=[[] for _ in range(k+1)]
visited=[[] for _ in range(k+1)]
length=[0]*(k+1)
for _ in range(n):
    x,y,color=map(int,input().split())
    arr[color].append((x,y))
    visited[color].append(0)
    length[color]+=1
# print(arr)
# print(visited)
# print(length)
pos=[0]*(k+1)
ans=sys.maxsize
def dfs(i):
    global k,visited,ans
    if i==k+1:
        max_x=-1000
        min_x=1000
        max_y=-1000
        min_y=1000
        for xv,yv in pos[1:]:
            if max_x<xv:
                max_x=xv
            if min_x>xv:
                min_x=xv
            if max_y<yv:
                max_y=yv
            if min_y>yv:
                min_y=yv
        area=abs((max_x-min_x)*(max_y-min_y))
        # print(pos,area)
        if  ans > area:
            ans=area
        return
    for j in range(length[i]):
        if not visited[i][j]:
            pos[i]=arr[i][j]
            visited[i][j]=1
            dfs(i+1)
            visited[i][j]=0        
dfs(1)

print(ans)
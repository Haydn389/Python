import sys,copy
input=sys.stdin.readline
from collections import deque
n=int(input())
a=[list(input().split()) for _ in range(n)]

teacher=[]
for i in range(n):
    for j in range(n):
        if a[i][j]=='X':
            a[i][j]=0
        elif a[i][j]=='T':
            a[i][j]=2
            teacher.append((i,j))
        else:
            a[i][j]=1

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x0,y0,temp):
    q=deque([(x0,y0)])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and (nx == x0 or ny==y0) and temp[nx][ny]<2:
                if temp[nx][ny]==1:
                    return False
                q.append((nx,ny))
                temp[nx][ny]=2
    return True        

def back(depth):
    if depth==3:
        check=True
        for x,y in teacher:
            temp=copy.deepcopy(a)
            if bfs(x,y,temp)==False:#한번이라도 false가 나오면 break
                return False
        return True
    for i in range(n): 
        for j in range(n):
             if a[i][j]==0:
                a[i][j]=3
                if back(depth+1):
                    return True
                a[i][j]=0
    return False

print("YES" if back(0) else "NO")
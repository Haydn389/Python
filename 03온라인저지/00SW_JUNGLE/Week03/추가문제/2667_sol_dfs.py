import sys
from collections import deque
input=sys.stdin.readline
n=int(input())

a = [list(map(int,list(input().rstrip()))) for _ in range(n)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
def dfs(num,x,y):
    a[x][y]=2
    print("*"*25)
    for p in a:
        print(*p)
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i] 
        if 0<=nx<n and 0<=ny<n and a[nx][ny]==1:
            num+=1
            num=dfs(num,nx,ny)
    return num

    # q=deque()
    # q.append((x,y))
    # num=0
    # a[x][y]=2 #!****방문처리하기 방문처리 안하니까 아래에서 한번 더 방문함
    # while q:
    #     x,y=q.popleft()
    #     num+=1
    #     for i in range(4):
    #         nx=x+dx[i]
    #         ny=y+dy[i] 
    #         if 0<=nx<n and 0<=ny<n and a[nx][ny]==1:
    #             a[nx][ny]=2
    #             q.append([nx,ny])
    #         print("*"*25)
    #         for p in a:
    #             print(*p)
    # return num

cnt=0
res=[]
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            cnt+=1
            num=0
            res.append(dfs(1,i,j))
print(cnt)

for r in sorted(res):
    print(r)
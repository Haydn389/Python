from collections import deque
from re import L   

n,m=map(int,input().split())

a=[list(input().rstrip()) for _ in range(n)]

print(a)


q=deque()

for i in range(n):
    for j in range(m):
        if a[i][j]=="*":
            q.append((i,j))

# print(q)
dx,dy=[1,-1,0,0],[0,0,1,-1]
def bfs():
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i] 
            if 0<=nx<n and 0<=ny<m and a[nx][ny]==".":
                a[nx][ny]=a[x][y]+"*"
                q.append((nx,ny))

bfs()
for k in a:
    for r in k:
        print("{:<7}".format(r),end="")
    print()
# print(a)


# for i in range(n):
#     for j in range(m):
#         if a[i][i]=='D':
#             pass

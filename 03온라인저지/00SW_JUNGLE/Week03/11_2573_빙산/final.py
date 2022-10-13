import sys,copy
input=sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

#방향
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    temp[x][y]=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i] 
            if 1<=nx<n-1 and 1<=ny<m-1 and temp[nx][ny]!=0:
                temp[nx][ny]=0
                q.append((nx,ny))

def melt(a):
    new_a=[[0]*m for _ in range(n)]
    for x in range(1,n-1):
        for y in range(1,m-1):
            water=0
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if a[nx][ny]==0:
                    water+=1
            # new_a[x][y]=a[x][y]-water
            ice=a[x][y]-water
            new_a[x][y]=ice if ice>0 else 0
    return new_a 

# print("="*50)
# for p in melt(a):
#     for k in p:
#         print(f"{k:<2}",end="")
#     print()

year=0
while True:
    cnt=0
    temp=copy.deepcopy(a)
    for i in range(1,n-1):
        for j in range(1,m-1):
            if temp[i][j]!=0:
                cnt+=1
                bfs(i,j)
    # print(cnt)
    if cnt==0:
        print(0)
        break
    elif cnt>1:
        print(year)
        break   
    a = copy.deepcopy(melt(a))
    year += 1
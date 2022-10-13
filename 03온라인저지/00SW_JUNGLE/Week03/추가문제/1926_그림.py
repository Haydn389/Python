import sys
input=sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6)


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(x,y):
    global num
    if x<0 or x>=n or y<0 or y>=m:
        return
    if a[x][y]==1:
        num+=1
        a[x][y]=2
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
    # print("*"*25)
    # for p in a:
    #     print(*p)
    # !*****아래 방법으로 하면 메모리초과
    # a[x][y]=2
    # num+=1
    # for i in range(4):
    #     nx=x+dx[i]
    #     ny=y+dy[i] 
    #     if 0<=nx<n and 0<=ny<m and a[nx][ny]==1:
    #         num=dfs(nx,ny,num)
    # return num


def bfs(x,y):
    num=0
    q=deque()
    q.append((x,y))
    a[x][y]=2
    while q:
        x,y=q.popleft()
        num+=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i] 
            if 0<=nx<n and 0<=ny<m and a[nx][ny]==1:
                a[nx][ny]=2
                q.append((nx,ny))
    return num

cnt=0
res=[]
for i in range(n):
    for j in range(m):
        if a[i][j]==1:
            cnt+=1
            num=0
            # res.append(bfs(i,j))
            dfs(i,j)
            res.append(num)

# print(cnt)
# print(res)
print(len(res))
if res:
    print(max(res))
else:
    print(0)
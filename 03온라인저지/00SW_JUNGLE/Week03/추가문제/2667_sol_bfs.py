import sys
from collections import deque
input=sys.stdin.readline
n=int(input())

a = [list(map(int,list(input().rstrip()))) for _ in range(n)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
def bfs(x,y):
    q=deque()
    q.append((x,y))
    num=0
    a[x][y]=2 #!****방문처리하기!!! 방문처리 안하니까 다음노드에서 시작노드를 한번 더 방문함
    while q:
        x,y=q.popleft()
        num+=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i] 
            if 0<=nx<n and 0<=ny<n and a[nx][ny]==1:
                a[nx][ny]=2
                q.append([nx,ny])
            print("*"*25)
            for p in a:
                print(*p)
    return num

cnt=0
res=[]
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            cnt+=1
            res.append(bfs(i,j))
print(cnt)

for r in sorted(res):
    print(r)
import sys
from collections import deque
input=sys.stdin.readline

n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
S, X, Y=map(int, input().split())
virus=[]
for i in range(n):
    for j in range(n):
        if a[i][j]!=0:
            virus.append((a[i][j],i,j,0))
virus.sort()
q=deque(virus)
# cnt=0
dx=[0,1,0,-1]
dy=[1,0,-1,0]
while q:
    v,x,y,cnt=q.popleft()
    if cnt==S:
        break
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i] 
        if 0<=nx<n and 0<=ny<n and a[nx][ny]==0:
            a[nx][ny]=v
            q.append((v,nx,ny,cnt+1))
    # cnt+=1
    # print("*"*50)
    # print(">>>cnt",cnt)
    # for p in a:
    #     print(*p)
print(a[X-1][Y-1])
'''
3 3
1 0 2
0 0 0
3 0 0
1 2 2
'''
#답 0
'''
3 3
1 0 2
0 0 0
3 0 0
2 3 2
'''
#답 3
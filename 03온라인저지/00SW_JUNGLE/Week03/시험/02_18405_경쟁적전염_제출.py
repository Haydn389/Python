import sys
input=sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
S, X, Y = map(int, input().split())

virus=[]
#뒤에서 sort()하기 위해서 큐가 아닌 리스트 먼저 선언 
for i in range(n):
    for j in range(n):
        if a[i][j]!=0:
            virus.append((a[i][j],i,j,0))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
#오름차순 정렬
virus.sort()
q=deque(virus)
while q:
    v,x,y,cnt=q.popleft()
    if cnt==S: #문제에서 요구한 시간이되면 break
        break
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i] 
        if 0<=nx<n and 0<=ny<n and a[nx][ny]==0:
            a[nx][ny]=v #해당 바이러스로 감염시키기
            q.append((v,nx,ny,cnt+1)) #시간 카운트
print(a[X-1][Y-1])
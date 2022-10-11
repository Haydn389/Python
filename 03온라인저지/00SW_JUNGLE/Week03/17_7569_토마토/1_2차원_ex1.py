from collections import deque
import sys
input=sys.stdin.readline
m,n=map(int,input().split())

a=[list(map(int,input().split())) for _ in range(n)]


queue = deque([])

dx,dy=[-1,1,0,0],[0,0,-1,1]

for i in range(n):
    for j in range(m):
        if a[i][j]==1:
            queue.append([i,j])


def bfs():
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx,ny=x+dx[i],dy[i]+y
            if 0<=nx<n and 0<=ny<m and a[nx][ny]==0:
                a[nx][ny]=a[x][y]+1          
                queue.append([nx,ny])
                # print("*"*50)
                # for k in a:
                #     print (*k)
bfs()
ans=0
# check=False
# for i in a:
#     for j in i:
#         if j==0:
#             check=True
#             break
#     if check:break
#     ans=max(ans,max(i))
# if check:
#     print(-1)
# else:
#     print(ans-1)

for i in a:
    for j in i:
        # 다 찾아봤는데 토마토를 익히지 못했다면 -1 출력
        if j == 0:
            print(-1)
            exit(0)
    # 다 익혔다면 최댓값이 정답
    ans = max(ans, max(i))
# 처음 시작을 1로 표현했으니 1을 빼준다.
print(ans - 1)
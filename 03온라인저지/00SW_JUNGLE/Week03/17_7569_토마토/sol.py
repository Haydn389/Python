from collections import deque
import sys
input = sys.stdin.readline
m, n, h = map(int, input().split())
a = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
# print(a)
queue = deque()
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if a[i][j][k] == 1:
                queue.append([i, j, k])
# print(queue)
def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
            if 0 <= nx < h and 0 <= ny < n and 0<=nz<m and a[nx][ny][nz] == 0:
                a[nx][ny][nz] = a[x][y][z]+1
                queue.append([nx, ny, nz])

bfs()
day = 0
for i in a:
    for j in i:
        for k in j:
            # 다 찾아봤는데 토마토를 익히지 못했다면 -1 출력
            if k == 0:
                print(-1)
                exit(0)
                flag=1
        day = max(day, max(j))
# 처음 시작을 1로 표현했으니 1을 빼준다.
print(day-1)

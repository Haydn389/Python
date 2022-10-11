import sys
import copy
# 10**6 이상 메모리초과, 10**4,10**5 통과, 10**3 이하 recursionerror
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def melt(a):
    new_a = [[0]*m for _ in range(n)]
    for x in range(1, n-1):
        for y in range(1, m-1):
            water = 0
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if a[nx][ny] == 0:
                    water += 1
            ice=a[x][y]-water
            new_a[x][y]=ice if ice>0 else 0
    return new_a

def dfs(x, y):
    if x <= 0 or x >= n-1 or y <= 0 or y >= m-1 or visited[x][y] == 0:
        return
    visited[x][y] = 0
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)

year = 0
while True:
    cnt = 0
    visited = copy.deepcopy(a)
    for i in range(1, n-1):
        for j in range(1, m-1):
            if visited[i][j] != 0:
                dfs(i, j)
                cnt += 1
    if cnt == 0:    # 빙하가 다 녹으면 종료F
        year = 0
        break
    elif cnt != 1:  # 둘로 쪼개지면 종료
        break
    a = copy.deepcopy(melt(a))
    year += 1

print(year)

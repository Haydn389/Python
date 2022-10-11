import sys
import copy
# 10**6 이상 메모리초과, 10**4,10**5 통과, 10**3 이하 recursionerror
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

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
            ice = a[x][y]-water
            new_a[x][y] = ice if ice > 0 else 0
    return new_a


def dfs(x, y):
    if x < 1 or y < 1 or x >= n-1 or y >= m-1 or temp[x][y] == 0:
        return
    temp[x][y] = 0
    dfs(x+1, y)
    dfs(x, y+1)
    dfs(x-1, y)
    dfs(x, y-1)


year = 0
while True:
    cnt = 0
    temp = copy.deepcopy(a)
    for i in range(1, n-1):
        for j in range(1, m-1):
            if temp[i][j] != 0:
                cnt += 1
                dfs(i, j)
    if cnt == 0:
        year = 0
        break
    if cnt != 1:
        break
    a = copy.deepcopy(melt(a))
    year += 1

print(year)

import sys
n, k = map(int, input().split())
color = [[] for i in range(k + 1)]
result = [987654321]

for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    color[c].append([a, b])

def dfs(lx, ly, hx, hy, cnt, current):
    if cnt == k + 1:
        if result[0] > current:
            result[0] = current
        return

    for point in color[cnt]:
        x1, x2, y1, y2 = lx, hx, ly, hy
        if point[0] < lx:
            x1 = point[0]
        elif point[0] > hx:
            x2 = point[0]
        if point[1] < ly:
            y1 = point[1]
        elif point[1] > hy:
            y2 = point[1]

        temp = abs(x2 - x1) * abs(y2 - y1)
        if temp < result[0]:
            dfs(x1, y1, x2, y2, cnt + 1, temp)


for p in color[1]:
    dfs(p[0], p[1], p[0], p[1], 2, 0)

print(result[0])
import sys
n = int(sys.stdin.readline())
w = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


visited = []
min_val = 1e9


def tsp(start, next, cost, visited):
    global min_val
    if len(visited) == n:
        if w[next][start] != 0:
            min_val=min(min_val,cost+w[next][start])
            return
    for i in range(n):
        if w[next][i] != 0 and i not in visited and cost < min_val:
            # 방문이 가능하고,
            visited.append(i)
            tsp(start, i, cost+w[next][i], visited)
            visited.pop()

for i in range(n):
    tsp(i, i, 0, [i])

print(min_val)

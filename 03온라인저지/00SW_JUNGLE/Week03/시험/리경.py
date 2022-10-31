import sys, heapq
n, k = map(int, sys.stdin.readline().split())
graph = []
q = []
for i in range(n):
    input = list(map(int, sys.stdin.readline().split()))
    graph.append(input)
    for j in range(n):
        if graph[i][j] != 0:
            heapq.heappush(q, [graph[i][j],i,j])
s,end_x,end_y = map(int, sys.stdin.readline().split())

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(virus, x, y):
    new_virus = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < n and 0<= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                new_virus.append([virus,nx,ny])
    print("="*50)
    for p in graph:
        print(*p)
    return new_virus

for _ in range(s): # 1초가 지날 때마다
    new = []
    while q:
        virus, x, y = heapq.heappop(q)
        new_virus = bfs(virus, x, y)
        print("bfs완료")
        new += new_virus
    for k in new:
        heapq.heappush(q, k)
    print("1초 지남")
print(graph[end_x-1][end_y-1])
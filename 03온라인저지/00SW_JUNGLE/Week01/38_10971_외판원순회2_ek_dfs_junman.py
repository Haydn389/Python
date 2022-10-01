import sys
N = int(sys.stdin.readline().strip())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().strip().split())))

visited = [False for _ in range(N)]

ans = 4000001

def travel_dfs(city, count, cost):
    if count == N-1:
        if visited[0] == True or board[city][0] == 0:
            return
        global ans
        ans = min(ans, cost+board[city][0])
        return

    for next_city, road_cost in enumerate(board[city]):
        if road_cost == 0:
            continue
        if not visited[next_city]:
            visited[next_city] = True
            travel_dfs(next_city, count+1, cost+road_cost)
            visited[next_city] = False

travel_dfs(0, 0, 0)
print(ans)

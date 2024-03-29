from collections import deque

def BFS():
    queue = deque()
    queue.append(N)
    while queue:
        present = queue.popleft()
        if present == K:
            print(dist[present])
            break
        for not_present in (present+1, present-1, present*2):
            if 0 <= not_present <= MAX and not dist[not_present]:
                dist[not_present] = dist[present] + 1
                queue.append(not_present)

MAX = 10 ** 5
dist = [0] * (MAX+1)
N, K = map(int, input().split())
BFS()
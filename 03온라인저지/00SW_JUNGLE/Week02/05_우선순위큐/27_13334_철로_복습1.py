import heapq
import sys
input = sys.stdin.readline
n = int(input())
a = [sorted(list(map(int, input().split()))) for _ in range(n)]
a.sort(key=lambda x: x[1])
d = int(input())
h = []
res = 0
for s, e in a:
    lim = e-d
    if lim <= s:
        heapq.heappush(h, s)
    while h and h[0] < lim:
        heapq.heappop(h)
    res = max(res, len(h))
print(res)

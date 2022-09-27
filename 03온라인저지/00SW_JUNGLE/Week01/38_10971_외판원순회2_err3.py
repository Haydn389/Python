import sys
from itertools import permutations
sys.setrecursionlimit(10**8)  # 10^8 까지 늘림.
m = n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# data=[[0, 10, 15, 20], [5, 0, 9, 10], [6, 13, 0, 12], [8, 8, 9, 0]]

ans = 1e9
all = permutations(list(range(n)))
for per in all:
    s = 0
    for k in range(n):
        s += data[per[k % n]][per[(k+1) % n]]
    if s < ans:
        ans = s
print(ans)


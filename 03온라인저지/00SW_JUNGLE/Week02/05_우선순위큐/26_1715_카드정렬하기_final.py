import sys
from heapq import heapify,heappop,heappush
input = sys.stdin.readline
n = int(input())

h = list(int(input()) for _ in range(n))

heapify(h)
res=0
while len(h)>1:
    a=heappop(h)
    b=heappop(h)
    res+=(a+b)
    heappush(h,a+b)

print(res)
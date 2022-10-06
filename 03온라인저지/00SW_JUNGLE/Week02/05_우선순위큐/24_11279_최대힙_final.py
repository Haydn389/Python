import heapq
import sys
input=sys.stdin.readline
n=int(input().rstrip())
h=[]
for _ in range(n):
    cmd=int(input())
    if cmd==0:
        if h:
            print(-heapq.heappop(h))
        else:print(0)
    else:
        heapq.heappush(h,-cmd)
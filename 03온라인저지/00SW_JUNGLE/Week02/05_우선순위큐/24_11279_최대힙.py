import heapq
import sys
input=sys.stdin.readline
n=int(input().rstrip())

h=[]
for _ in range(n):
    cmd=int(input().rstrip())
    if cmd==0:
        try: print(-heapq.heappop(h))
        except:
            print(0)

    else:
        heapq.heappush(h,-cmd)
    
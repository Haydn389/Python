import heapq
from heapq import heapify
import sys
input=sys.stdin.readline
n=int(input().rstrip())

h=[]
for _ in range(n):
    h.append(int(input().rstrip()))
    # num=int(input().rstrip())
    # heapq.heappush(h,num)
heapify(h)
print(h)


# print(h)
# res=0
# for _ in range(n):
#     res+=heapq.heappop(h)



# print(res)
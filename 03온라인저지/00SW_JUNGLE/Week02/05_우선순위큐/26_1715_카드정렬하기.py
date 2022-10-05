import heapq
import sys
input=sys.stdin.readline

n=int(input())

h=[]
for _ in range(n):
    num=int(input())
    heapq.heappush(h,num)
res=0

while len(h)>1:
    a=heapq.heappop(h)
    b=heapq.heappop(h)
    res+=(a+b)
    heapq.heappush(h,a+b)


print(res)
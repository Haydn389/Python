import heapq
import sys
input=sys.stdin.readline

n=int(input())
h=list(int(input()) for _ in range(n))
heapq.heapify(h)

# h=[]
# for _ in range(n):
#     num=int(input())
#     heapq.heappush(h,num)

res=0
while True:
    a=heapq.heappop(h)
    b=heapq.heappop(h)
    res+=(a+b)
    if len(h)==0:break
    heapq.heappush(h,a+b)


print(res)
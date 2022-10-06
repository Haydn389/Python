import sys
from heapq import heapify,heappop,heappush

input=sys.stdin.readline
h=[]

n=int(input())

for _ in range(n):
    a=list(map(int,input().split()))

    if len(h)==0:
        for i in a:
            heappush(h,i)
    else:
        for i in a:
            if h[0]<i:
                heappush(h,i)
                heappop(h)
print(h[0])
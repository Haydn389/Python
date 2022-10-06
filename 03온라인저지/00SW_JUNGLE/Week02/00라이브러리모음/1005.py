import sys
from heapq import heapify,heappop,heappush
input=sys.stdin.readline
n=int(input())
h=list(map(int,input().split()))
heapify(h)
for _ in range(n-1):
    a=list(map(int,input().split()))
    for num in a:
        if h[0]<num:    #큰값을 계속해서 넣는다.
            heappush(h,num)
            heappop(h)
            
print(h[0])
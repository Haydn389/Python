from heapq import heapify,heappop,heappush
import sys
input = sys.stdin.readline
k,n = map(int,input().split())
a = list(map(int, input().split()))

h=[*a]
heapify(h)

for _ in range(n):
    num=heappop(h)
    for i in range(k):
        temp=num*a[i]
        heappush(h,temp)
        if num%a[i]==0:
            break
    print(num)
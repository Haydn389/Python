from heapq import heapify,heappop,heappush
import sys
input = sys.stdin.readline
k,n = map(int, input().split())
a = list(map(int, input().split()))

# k,n=4,19
# a=[2,3,5,7]
h=[*a]
heapify(h)
res=None
for i in range(n):
    num=heappop(h)
    for i in range(k):
        temp=num*a[i]
        heappush(h,temp)
        if num%a[i]==0:break
    res=num
print(res)
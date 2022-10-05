import sys
input=sys.stdin.readline
import heapq
# n,k=map(int,input().split())
# a=list(map(int, input().split()))
k,n=4,19
a=[2,3,5,7]
#27
h=[*a]
# print(a)
heapq.heapify(h)
for _ in range(n):
    num=heapq.heappop(h)
    print(">>>",num)
    for i in range(k):
        temp=num*a[i]
        # print("**temp",temp)
        heapq.heappush(h,temp)
        if num%a[i]==0:
            break
print(num)

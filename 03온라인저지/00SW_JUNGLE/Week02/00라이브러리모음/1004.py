from bisect import bisect_left

import sys
input=sys.stdin.readline
n=int(input())
a= list(map(int,input().split()))

print(a)
res=[a[0]]

for i in range(n):
    if a[i]>res[-1]:
        res.append(a[i])
    else:
        x=bisect_left(res,a[i])
        res[x]=a[i]
print(res)
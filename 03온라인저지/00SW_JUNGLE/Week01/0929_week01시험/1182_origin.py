from itertools import combinations
import sys

n, m = map(int, sys.stdin.readline().split())
a=list(map(int,sys.stdin.readline().split()))
# n=5
# m=0
# a=[-7,-3,-2,5,8]
# print(n,m)
# print(a)

# all = list(combinations(a,3))
cnt=0
for i in range(1,n+1):
    for com in list(combinations(a,i)):
        # print(com)
        # print(sum(com))
        if sum(com)==m:
            cnt+=1

print(cnt)
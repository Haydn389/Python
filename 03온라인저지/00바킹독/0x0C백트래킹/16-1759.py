import sys
input=sys.stdin.readline
from itertools import combinations

n,m=map(int,input().split())
a=input().split()

# print(a)
res=[]
s=set(['a','e','i','o','u'])
for i in combinations(a,n):
    # if 2<= len(set(i)-s) <= n:
        res.append(sorted(i))

for j in sorted(res):
    if 2<=len(set(j)-s)<n:
        print("".join(j))
    # print(">>>",len(set(j)-s))
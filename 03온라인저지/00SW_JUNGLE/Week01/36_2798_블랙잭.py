import sys
from itertools import combinations
n,m=map(int,sys.stdin.readline().split())
a=list(map(int,sys.stdin.readline().split()))


b=list(combinations(a,3))

c=[sum(i) for i in b if sum(i)<=m]
print(max(c))
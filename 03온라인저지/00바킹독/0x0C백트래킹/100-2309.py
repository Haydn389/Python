import sys
from itertools import combinations
input=sys.stdin.readline
a=[]
for _ in range(9):
    a.append(int(input()))

res=[]
for i in combinations(a,7):
    if sum(i)==100:
        for j in sorted(list(i)):
            print(j)
        break
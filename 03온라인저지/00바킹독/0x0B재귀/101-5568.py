import sys
from itertools import permutations
input=sys.stdin.readline

n=int(input())
k=int(input())
a=[]
for i in range(n):
    a.append(input().rstrip())

res=set()
for i in permutations(a,k):
    res.add(''.join(i))

print(len(set(res)))

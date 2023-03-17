#중복조합
from itertools import combinations_with_replacement
import sys
input=sys.stdin.readline

n,m=map(int,input().split())

for i in combinations_with_replacement(list(range(1,n+1)),m):
    print(*i)
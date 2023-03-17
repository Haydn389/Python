from itertools import permutations
from itertools import combinations
import sys
input=sys.stdin.readline
n,m=map(int,input().split())

# for i in permutations(range(1,n+1),m):
#     print(i)
# print("-"*50)
for i in combinations(range(1,n+1),m):
    print(*i)
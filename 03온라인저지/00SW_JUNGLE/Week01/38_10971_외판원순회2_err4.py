import sys
from itertools import permutations
 
input = sys.stdin.readline
INF = 10*9
n = int(input())
w = [list(map(int,input().split())) for _ in range(n)]
 
all = permutations(list(range(n)))
 
ans = float('inf')
for p in all:
    cost = 0
    flag = True
    for i in range(n-1):
        tmp = w[p[i]][p[i+1]]
        if tmp == 0:
            flag = False
            break
        else: cost+=tmp
    tmp = w[p[n-1]][p[0]]
    if tmp ==0:
        flag = False
    else: cost+=tmp
    if flag and ans>cost:
        ans=cost
 
print(ans)
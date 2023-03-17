from itertools import combinations
import sys
input= sys.stdin.readline
n,s=map(int,input().split())

a=list(map(int,input().split()))
cnt=0
for i in range(1,n+1):
    for j in list(combinations(a,i)):
        if s==sum(j):cnt+=1

print(cnt)
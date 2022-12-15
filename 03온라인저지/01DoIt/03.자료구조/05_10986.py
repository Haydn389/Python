import sys
from itertools import combinations #조합

input=sys.stdin.readline

n,k=map(int,input().split())

a=list(map(int,input().split()))

s=[0]*(n+1)
c=[0]*k #m은 k미만
cnt=0

for i in range(n):
    s[i+1]=s[i]+a[i]

for i in range(n):
    temp=(s[i]+a[i])%k
    if temp==0:cnt+=1
    # s[i]=temp
    c[temp]+=1

for i in range(k):
    if c[i]>1:
        cnt+=(c[i]*(c[i]-1)//2)
print(cnt)
        
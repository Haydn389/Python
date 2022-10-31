import sys
input=sys.stdin.readline
n,m=map(int,input().split())

a=[0]+list(map(int,input().split()))
s=[0]*(n+1)
s[0]=0
for i in range(1,n+1):
    s[i]=s[i-1]+a[i]
# print(a)
# print(s)
for _ in range(m):
    a,b=map(int,input().split())
    print(s[b]-s[a-1])
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=[0]+list(map(int,input().split()))
s=[0]*(n+1)


for i in a:
    temp

s[1]=a[1]

print(a)
print(s)
for i in range(2,n+1):
    s[i]=s[i-1]+a[i]
for _ in range(m):
    a,b=map(int,input().split())
    print(s[b]-s[a-1])
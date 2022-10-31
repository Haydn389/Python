import sys
input=sys.stdin.readline

n=int(input())
a=[0]+list(map(int, input().split()))

d=[0]*(n+1)

d[1]=a[1]
d[2]=max(a[1],a[2])

for i in range(3,n+1):
    d[i]=max(d[i-1],d[i-2]+a[i])

print(d)
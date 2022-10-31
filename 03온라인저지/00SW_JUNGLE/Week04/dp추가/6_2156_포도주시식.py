import sys
input=sys.stdin.readline
n=int(input())

a=[0]*(n+2)

for i in range(1,n+1):
    a[i]=int(input())

# print(a)
d=[0]*10001
# d=[0]*(n+1)
d[1]=a[1]
d[2]=a[1]+a[2]

for i in range(3,n+1):
    d[i]=max(d[i-1],d[i-2]+a[i],d[i-3]+a[i-1]+a[i])

# print(d)

print(d[n])
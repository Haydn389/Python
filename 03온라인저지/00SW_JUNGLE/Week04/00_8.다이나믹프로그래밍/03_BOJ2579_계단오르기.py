import sys
input=sys.stdin.readline

n=int(input())
a=[]
for _ in range(n):
    a.append(int(input()))

d=[[0]*2 for _ in range(300)]

if n==1:
    print(a[0])
    exit(0)

d[0][0]=a[0]
d[0][1]=0
d[1][0]=a[1]
d[1][1]=a[1]+a[0]
for k in range(2,n):
    d[k][0]=max(d[k-2][0], d[k-2][1])+a[k]
    d[k][1]=d[k-1][0]+a[k]
print(max(d[n-1][0],d[n-1][1]))
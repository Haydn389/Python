import sys
input=sys.stdin.readline
n=int(input())
a=[0]*301
for i in range(1,n+1):
    a[i]=int(input())
# print(a)

d=[[0]*3 for _ in range(301)]

d[1][1]=a[1]
d[1][2]=a[1]
d[2][1]=a[1]+a[2]
d[2][2]=a[2]
for i in range(3,n+1):
    d[i][1]=d[i-1][2]+a[i]
    d[i][2]=max(d[i-2][1],d[i-2][2])+a[i]

# print(d)
print(max(d[n][1],d[n][2]))
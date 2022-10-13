import sys
input=sys.stdin.readline
n=int(input())

a=[0]*10001

a[0]=1
a[1]=2

for i in range(2,n):
    a[i]=(a[i-1]+a[i-2])% 15746
    # print(a)

print(a[n])
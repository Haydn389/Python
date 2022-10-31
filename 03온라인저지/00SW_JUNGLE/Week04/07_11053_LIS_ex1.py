import sys
input=sys.stdin.readline

n=int(input())
a=[0]+list(map(int,input().split()))

d=[0]*(n+1)
d[1]=1
for i in range(2,n+1):
    temp=[0]
    for j in range(1,i):
        if a[j]<a[i]:
            temp.append(d[j])
    d[i]=max(temp)+1
print(max(d))
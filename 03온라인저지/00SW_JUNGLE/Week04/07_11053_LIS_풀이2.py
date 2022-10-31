import sys
input=sys.stdin.readline
n=int(input())
a=[0]+list(map(int,input().split()))

d=[0]*(n+1)
# d[1]=1 반례
# 7
# 8 9 10 1 2 3 4
ans=0
for i in range(1,n+1):
    for j in range(0,i):
        if a[j]<a[i]:
            d[i]=max(d[i],d[j]+1)
    # print(d)
    ans=max(ans,d[i])
# print(d)
print(ans)

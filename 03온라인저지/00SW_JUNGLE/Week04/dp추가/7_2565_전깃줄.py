import sys
input=sys.stdin.readline
n=int(input())

a=[[0,0]]
for _ in range(n):
    a.append(list(map(int,input().split())))

a.sort()
b=[i[1] for i in a]

dp=[1]*(n+1)
# dp[1]=1
for i in range(2,n+1):
    for j in range(1,i):
        if b[j]<b[i]:
            dp[i]=max(dp[i],dp[j]+1)
        # print(dp)
print(n-max(dp))
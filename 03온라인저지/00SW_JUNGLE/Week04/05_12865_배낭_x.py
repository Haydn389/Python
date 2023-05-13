import sys
input=sys.stdin.readline

n,k=map(int,input().split())
wt=[0]
val=[0]

for _ in range(n):
   a,b=map(int,input().split())
   wt.append(a)
   val.append(b)

d=[[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for w in range(1,k+1):
        if wt[i]>w:
            d[i][w]=d[i-1][w]
        else:
            d[i][w]=max(d[i-1][w],d[i-1][w-wt[i]]+val[i])

print(d[n][k])
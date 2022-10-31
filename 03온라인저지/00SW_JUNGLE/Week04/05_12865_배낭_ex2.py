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
    for j in range(1,k+1):
        if wt[i]>j:
            d[i][j]=d[i-1][j]
        else:
            d[i][j]=max(d[i-1][j],d[i-1][j-wt[i]]+val[i])

# for p in d:
#     print(p)

print(d[n][k])
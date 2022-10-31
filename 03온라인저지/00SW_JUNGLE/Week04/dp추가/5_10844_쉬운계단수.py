import sys
input=sys.stdin.readline
n=int(input())

d=[[0]*(10) for _ in range(n+1)]

for i in range(1,10):
    d[0][i]=1


for i in range(1,n+1):
    for j in range(10):
        if j==0:
            d[i][j]=(d[i-1][j+1])
        elif j==9:
            d[i][j]=d[i-1][j-1]
        else:
            d[i][j]=(d[i-1][j-1]+d[i-1][j+1])
# for p in d:
#     print(p)
print(sum(d[n-1])%10**9)
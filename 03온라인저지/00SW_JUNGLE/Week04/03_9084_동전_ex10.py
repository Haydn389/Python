import sys
input=sys.stdin.readline
t=int(input())

for _ in range(t):
    n=int(input())
    coin=list(map(int,input().split()))
    k=int(input())

    d=[[0]*(k+1) for _ in range(n+1)]

    for i in range(1,n+1):
        d[i][0]=1

    for i in range(1,n+1):
        for j in range(i,k+1):
            d[i][j]=d[i-1][j]+d[i][j-coin[i-1]]

    # for p in d:    
    #     print(p)
    if n>=k:
        print(d[k][k])
    else:
        print(d[n][k])

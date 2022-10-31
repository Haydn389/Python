import sys
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n=int(input())

    a=[0]+list(map(int,input().split()))
    sub=[0]*(n+1)
    for i in range(1,n+1):
        sub[i]=sub[i-1]+a[i]
    # print(sub)
    d=[[0]*(n+1) for _ in range(n+1)]

    # for dia in range(1,n+1):
    for dia in range(1,n):
        for start in range(1,n-dia+1):
            end=start+dia
            temp=[]
            # for k in range(start,end+1):
            for k in range(start,end):
                temp.append(d[start][k]+d[k+1][end]+sub[end]-sub[start-1])
            d[start][end]=min(temp)
    # for p in d:
    #     print(*p)

    print(d[1][n])

        
import sys
input=sys.stdin.readline
n=int(input())
a = [list(map(int, input().split())) for _ in range(n)]

d=[[-1]*n for _ in range(n)]
res=[[-1]*n for _ in range(n)]

d[n-1][n-1]=0

size=n-1
for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        # print(i,j)
        if i==n-1 and j==n-1:
            continue
        ni=i+a[i][j]
        nj=j+a[i][j]
        if 0<=ni<n and d[ni][j]>=0:
            # d[i][j]=d[ni][j]+1
            d[i][j]=0
        if 0<=nj<n and d[i][nj]>=0:
            # d[i][j]=d[i][nj]+1
            d[i][j]=0

print("_"*50)
for p in d:
    print(p)

# d[n-1][n-1]=1
for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        # print(i,j)
        if i==n-1 and j==n-1:
            continue
        ni=i+a[i][j]
        nj=j+a[i][j]
        if 0<=ni<n and d[ni][j]>=0:
            d[i][j]=d[ni][j]+1
            # d[i][j]=0
        if 0<=nj<n and d[i][nj]>=0:
            d[i][j]=d[i][nj]+1
            # d[i][j]=0

print(d[0][0])

print("_"*50)
for p in d:
    print(p)
# print(max_val)
import sys
input=sys.stdin.readline

n,k=map(int,input().split())

stuff=[[0,0]]

for _ in range(n):
    stuff.append(list(map(int,input().split())))

stuff.sort(key=lambda x:x[0])

print(stuff)

d=[[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for W in range(1,k+1):
        if stuff[i][0] > W:
            d[i][W]=d[i-1][W]
        else:
            d[i][W]=max(d[i-1][W],d[i-1][W-stuff[i][0]]+stuff[i][1])

for p in d:
    print(p)

print(d[n][k])
import sys
input=sys.stdin.readline

n,k=map(int,input().split())

stuff=[[0,0]]
for _ in range(n):
    stuff.append(list(map(int,input().split())))

# stuff.sort()
# print(stuff)
d=[[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        if j<stuff[i][0]:
            d[i][j]=d[i-1][j]
        else:
            d[i][j]=max(d[i-1][j],d[i-1][j-stuff[i][0]]+stuff[i][1])

# for p in d:
#     print(*p)
print(d[n][k])

import sys
n,m=map(int,sys.stdin.readline().split())
data=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]




# print(data)
for i in range(n):
    for j in range(m):
        print(data[i][j],end=' ')
    print()
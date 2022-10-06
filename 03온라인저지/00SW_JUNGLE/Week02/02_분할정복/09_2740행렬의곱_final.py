import sys
input=sys.stdin.readline
n,m=list(map(int,input().split()))
a=[list(map(int,input().split())) for _ in range(n)]

m,k=list(map(int,input().split()))
b=[list(map(int,input().split())) for _ in range(m)]

new=[[None]*k for _ in range(n)]


for row in range(n):
    for col in range(k):
        temp=0
        for i in range(m):
            temp+=a[row][i]*b[i][col]
        new[row][col]=temp

for i in new:
    print(*i)
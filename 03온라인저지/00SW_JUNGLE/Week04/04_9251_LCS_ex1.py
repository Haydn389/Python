import sys
input=sys.stdin.readline
a=input().rstrip()
b=input().rstrip()

n=len(a)
m=len(b)

d=[[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i-1]==b[j-1]:
            d[i][j]=d[i-1][j-1]+1
        else:
            d[i][j]=max(d[i-1][j],d[i][j-1])

# for p in d:
#     print(*p)

print(d[n][m])
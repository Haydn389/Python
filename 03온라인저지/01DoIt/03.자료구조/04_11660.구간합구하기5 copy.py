import sys

input=sys.stdin.readline

n,m=map(int,input().split())

a = [list(map(int, input().split())) for _ in range(n)]
s=[[0]*(n+1) for _ in range(n+1)]
res=0
# for i in range(n):
#     for j in range(n):
#         if j==0:
#             s[i+1][j+1]=s[i][n]+a[i][j]
#         else:
#             s[i+1][j+1]=s[i+1][j]+a[i][j]

for i in range(n):
    for j in range(n):
        s[i+1][j+1]=s[i+1][j]+s[i][j+1]-s[i][j]+a[i][j]

# for p in s:
#     print(p)                           
res=0
for _ in range(m):
    x1,y1,x2,y2=map(int,input().split())
    res=s[x2][y2]-s[x2][y1-1]-s[x1-1][y2]+s[x1-1][y1-1]
    print(res)


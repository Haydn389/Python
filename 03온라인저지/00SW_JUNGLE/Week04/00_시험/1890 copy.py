import sys
input=sys.stdin.readline
n=int(input())
# a = [list(map(int, input().split())) for _ in range(n)]

d=[[-1]*n for _ in range(n)]

d[n-1][n-1]=0

# size=n-1
# for i in range(n-1,-1,-1):
#     for j in range(n-1,-1,-1):
#         d[start][end]
cnt=0
for dia in range((n-2)*2,-1,-1):
    for i in range((n-1),-1,-1):
        j=dia-i
        cnt+=1
        print(i,j)
#         d[i][j]=cnt
# for p in d:
#     print(p)
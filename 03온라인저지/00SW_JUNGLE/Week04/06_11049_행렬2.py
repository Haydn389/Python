import sys
input=sys.stdin.readline
n=int(input())
mat=[[0,0]]
for _ in range(n):
    mat.append(list(map(int,input().split())))
d=[[0]*(n+1) for _ in range(n+1)]
# print(mat)
for i in range(1,n+1):
    start=0
    for end in range(i+1,n+1):
        start+=1
        d[start][end]=sys.maxsize
        for k in range(start,end): #k는 s부터 e-1까지
            d[start][end]=min(d[start][end],d[start][k]+d[k+1][end]+mat[start][0]*mat[k][1]*mat[end][1])
print(d[1][n])
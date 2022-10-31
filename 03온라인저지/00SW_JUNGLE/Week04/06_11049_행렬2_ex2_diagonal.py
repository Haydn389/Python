import sys
input=sys.stdin.readline

n=int(input())

mat=[[0,0]]+[list(map(int,input().split())) for _ in range(n)]

# print(mat)
d=[[0]*(n+1) for _ in range(n+1)]

for diagonal in range(1,n):
    for start in range(1,n-diagonal+1):
        end=start+diagonal
        temp=[]
        for k in range(start,end): #i=3 일때 k=1,2,3
            temp.append(d[start][k]+d[k+1][end]+mat[start][0]*mat[k][1]*mat[end][1])
        d[start][end]=min(temp)
        # d[start][end]=start


for p in d:
    for o in p:
        print(f"{o:>5}",end=" ")
    print()

print(d[1][n])
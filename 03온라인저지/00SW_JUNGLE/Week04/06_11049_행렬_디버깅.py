import sys
input=sys.stdin.readline
n=int(input())
# row=[[0]]
# col=[[0]]
mat=[[0,0]]
for _ in range(n):
    mat.append(list(map(int,input().split())))
d=[[0]*(n+1) for _ in range(n+1)]
# print(mat)
for i in range(1,n+1):
    start=0
    for end in range(i+1,n+1):
        start+=1
        temp=[]
        for k in range(start,end): #k는 s부터 e-1까지
            # print(start,k,"&&",k+1,end)
            print(f"d[{start}][{k}]",d[start][k],f"d[{k+1}][{end}]",d[k+1][end])
            print("mat : ",mat[start][0]*mat[k][1]*mat[end][1])
            # print(d[start][k],d[k+1][end],mat[start][0]*mat[k][1]*mat[end][1])
            temp.append(d[start][k]+d[k+1][end]+mat[start][0]*mat[k][1]*mat[end][1])
        print(temp)
        d[start][end]=min(temp)
        # d[start][end]=start
        print("*"*20)

for p in d:
    for o in p:
        print(f"{o:>5}",end=" ")
    print()

print(d[1][n])
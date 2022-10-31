import sys
input=sys.stdin.readline
n=int(input())
# row=[[0]]
# col=[[0]]
mat=[[0,0]]
for _ in range(n):
    mat.append(list(map(int,input().split())))
d=[[0]*(n+1) for _ in range(n+1)]
print(mat)
for i in range(1,n+1):
    for j in range(i+1,n+1):
        # d[i][j]='x'
        temp=[]
        for k in range(i,j):
            print(f"i:{i}, j:{j}, k:{k}")
            # mat[j][1]=1
            temp.append(d[i][k]+d[k+1][j]+mat[i][0]*mat[k][1]*mat[j][1])
            # print(d[i][j], d[i][k]+d[k+1][j]+mat[i][0]*mat[k][1]*mat[j][1])
        d[i][j]=min(temp)
        # d[i][j]=min(temp)
        print("*"*20)

for p in d:
    for o in p:
        print(f"{o:<2}",end=" ")
    print()

        # print(i,j)
        # if i>=j:
        #     d[i][j]=0
        #     continue
# print(d)
# print(mat)
import sys
n,m=map(int,sys.stdin.readline().split())

##방법1
data=[]
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))

##방법2
# data=[[0]*m for _ in range(n)]
# for i in range(n):
#     data[i]=list(map(int,sys.stdin.readline().split()))

print()

for i in range(m):
    for j in range(n):
        print(data[i][j],end=" ")
    print()
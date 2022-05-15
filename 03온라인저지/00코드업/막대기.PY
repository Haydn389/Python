import sys
k=int(sys.stdin.readline().strip())
# n,m=map(int,sys.stdin.readline().split())
w=[[]*2 for _ in range(k)]
for i in range(k):
    w[i]=list(map(int,sys.stdin.readline().split()))

# print(w)

n=19
m=19

arr=[[0]*m for _ in range(n)]
for i in w:
    x,y=i
    arr[x-1][y-1]=1


# for i in range(len(w)):
#     arr[w[i][0]-1][w[i][1]-1]=1


for i in range(n):
    for j in range(m):
        print(arr[i][j],end=" ")
    print()
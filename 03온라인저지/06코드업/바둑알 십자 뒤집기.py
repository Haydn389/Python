import sys
arr=[]
n=m=19
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))


k=int(sys.stdin.readline().strip())
for i in range(k):
    x,y=map(int,sys.stdin.readline().split())
    for r in range(n):
        if arr[x-1][r]==0:
            arr[x-1][r]=1
        else:arr[x-1][r]=0
    for c in range(n):
        if arr[c][y-1]==0:
            arr[c][y-1]=1
        else:arr[c][y-1]=0

    # print(x,y)

for i in range(n):
    for j in range(m):
        print(arr[i][j],end=" ")
    print()
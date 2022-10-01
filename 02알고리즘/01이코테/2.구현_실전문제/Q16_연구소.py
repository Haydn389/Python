import sys

n,m=map(int,sys.stdin.readline().split())

arr=[]


for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))


print()


for i in range(n):
    for j in range(m):
        print(arr[i][j],end=" ")
    print()
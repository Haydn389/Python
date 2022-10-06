import sys
input=sys.stdin.readline

n,b=list(map(int,input().split()))
a=[list(map(int,input().split())) for _ in range(n)]

# print(n,b)
# print(a)

def matrix(a,b):
    global n
    # n=len(a)
    new=[[0]*n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            temp=0
            for i in range(n):
                temp+=a[row][i]*b[i][col]
            new[row][col]=temp%1000
    return new

def sol(a,b):
    global n
    if b==1:
        for i in range(n):
            for j in range(n):
                a[i][j]%=1000
        return a
    temp=sol(a,b//2)
    if b%2==0:
        return matrix(temp,temp)
    else:
        return matrix(matrix(temp,temp),a)

ans=sol(a,b)
for i in ans:
    print(*i)

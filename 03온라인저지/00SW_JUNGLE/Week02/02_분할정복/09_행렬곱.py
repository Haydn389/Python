import sys
input=sys.stdin.readline
# n,b=list(map(int,input().split()))

# m=[list(map(int,input().split())) for _ in range(n)]

n=3
m=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_m=[[0]*n for _ in range(n)]
for row in range(n):
    for col in range(n):
        temp=0
        for i in range(n):
            temp+=m[row][i]*m[i][col]
            #    temp+=m[i][j]*m[j][i]
        new_m[row][col]=temp

print(new_m)
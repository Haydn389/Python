import sys
n,m = map(int,sys.stdin.readline().split(" "))

a = [[0]*(n+1)]

for i in range(n):
    a.append([0]+list(map(int,sys.stdin.readline().split())))
# print("*"*50)
s=[[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        s[i][j]=s[i-1][j]+s[i][j-1]-s[i-1][j-1]+a[i][j]


# # print(a)
# for i in range(n+1):
#     for j in range(n+1):
#         print("{:<5}".format(a[i][j]),end=' ')
#     print()
# print("-"*50)

# for i in range(n+1):
#     for j in range(n+1):
#         print("{:<5}".format(s[i][j]),end=' ')
#     print()

#질문값 받아서 출력
for _ in range(m):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    result=s[x2][y2]-s[x2][y1-1]-s[x1-1][y2]+s[x1-1][y1-1]
    print(result)
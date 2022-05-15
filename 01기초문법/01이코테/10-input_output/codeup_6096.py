import sys
n,m=19,19
data=[[]*m for _ in range(n)]

for i in range(n):
    data[i]=list(map(int,sys.stdin.readline().split())) #한 줄에 입력된 원소들을 리스트화 시켜줌
a = int(sys.stdin.readline())

for i in range(a):
    b,c = map(int,sys.stdin.readline().split())
    for j in range(19):
        if (data[b-1][j]==0):
            data[b-1][j]=1
        else:
            data[b-1][j]=0

    for j in range(19):
        if (data[j][c-1]==0):
            data[j][c-1]=1
        else:
            data[j][c-1]=0


# print()
for i in range(n):
    for j in range(m):
        print(data[i][j],end=' ')
    print()

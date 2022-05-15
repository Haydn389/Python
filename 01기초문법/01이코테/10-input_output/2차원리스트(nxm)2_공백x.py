import sys
n,m=map(int,sys.stdin.readline().split())
data=[]
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().strip()))) #한 줄에 입력된 원소들을 리스트화 시켜줌

# print(data)
for i in range(n):
    for j in range(m):
        print(data[i][j],end=' ')
    print()
import sys
data = []
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))

print(data)
# for i in range(n):
#     for j in range(m):
#         print(data[i][j],end=' ')
#     print()
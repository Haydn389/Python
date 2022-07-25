# import sys

# n=int(sys.stdin.readline().strip())
# data=[]
# for _ in range(n):
#     data.append(list(map(int,sys.stdin.readline().split())))

# # print(data)

# for i in range(n):
#     data[i]=[ c for c in data[i] if c %2!=0]
#     print("#"+str(i+1),sum(data[i]))

import sys

n=int(input().strip())
data=[]
for _ in range(n):
    data.append(list(map(int,input().split())))

# print(data)

for i in range(n):
    data[i]=[ c for c in data[i] if c %2!=0]
    print("#"+str(i+1),sum(data[i]))


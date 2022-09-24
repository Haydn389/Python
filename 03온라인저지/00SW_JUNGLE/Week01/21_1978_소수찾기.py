# https://youtu.be/CyINCmJPjfM
import math
n=int(input())
data=list(map(int,input().split()))

cnt=0

# def solve(k):
#     for i in range(2, k):
#         if k % i == 0:
#             return 0
#     return 1
# for a in data:
#     if a==1:continue
#     cnt+=solve(a)

for i in data:
    if i==1:continue
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            break
    else:
        cnt += 1
print(cnt)


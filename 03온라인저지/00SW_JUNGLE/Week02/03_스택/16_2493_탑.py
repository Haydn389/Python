#https://velog.io/@boorook/Python-%EB%B0%B1%EC%A4%80-2493-%ED%83%91-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4

import sys
input=sys.stdin.readline
# n=int(input())
# a=list(map(int,input().split()))
n=5
a=[6,9,5,7,4]
# a=[15,5,13,8,7]
stack=[] # [[],[]] 2차원리스트로 만들어서 앞에는 index+1,뒤에는 값을 저장
res=[0]*n

for i in range(n):
    while stack and stack[-1][1]<=a[i]:
        stack.pop()
    if stack:
        res[i]=stack[-1][0]

    stack.append([i+1,a[i]])
print(*res)
    

# 시간초과
# for i in range(n):
#     temp=0
#     for j in range(i):
#         if a[j]>a[i]:
#             temp=j+1
#     print(temp,end=" ")
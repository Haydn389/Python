# https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-2740-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%96%89%EB%A0%AC-%EA%B3%B1%EC%85%88-%EB%B8%8C%EB%A1%A0%EC%A6%881-%EC%84%A0%ED%98%95%EB%8C%80%EC%88%98
# a행 b열 x c행 d열
# 행렬 곱이 가능하기위해서는 b==c 이어야함!!

import sys
input=sys.stdin.readline
n,m=list(map(int,input().split()))
a=[list(map(int,input().split())) for _ in range(n)]

m,k=list(map(int,input().split()))
b=[list(map(int,input().split())) for _ in range(m)]

# a=[[1, 4], [2, 5], [3, 2]]
# b=[[2,3,2], [3,4,1]]
new=[[0]*k for _ in range(n)] #n행 k열

for row in range(n):
    for col in range(k):
        temp=0
        for i in range(m):
            temp+=a[row][i]*b[i][col]
        new[row][col]=temp

for i in new:
    print(*i)

import sys
from itertools import permutations
n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# data=[[0, 10, 15, 20], [5, 0, 9, 10], [6, 13, 0, 12], [8, 8, 9, 0]]
# n=4
ans = 1e9
all = permutations(list(range(n)))
# print(list(all))
# print(list(range(n)))
for per in all:
    flag=True               #도시 이동간 비용이0인지점이 있었는지 검사
    cost = 0                #현재 Case에서의 총 비용
    for k in range(n):      #도시를 돌며 비용 저장
        temp = data[per[k]][per[(k+1) % n]] #1개의 경로상 비용을 임시저장
        if temp ==0:        #도시 이동간 비용이 0이면 for문 탈출
            flag=False 
            break
        else: cost+=temp    #아니면 비용 저장
    if flag and ans>cost:   #flag검사를통해 도시 이동간 비용이0인지점이 있었는지 검사
        ans=cost            #그리고 비용이 이전단계 비용보다 적다면 교체
print(ans)


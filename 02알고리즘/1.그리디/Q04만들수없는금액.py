import time
import sys
from itertools import combinations, permutations
n = int(sys.stdin.readline().strip())

nums = list(map(int,sys.stdin.readline().split()))   #int
start = time.time()  # 시작 시간 저장
def solution(n,nums):

    com=[]
    for i in range(1,len(nums)+1):  #예) 325라고하면 i를 1~3까지 변화시키며 각각 1개, 2개, 3개 일때의 순열을 모두 출력
        com+=list(combinations(nums,i))


    print(com)
    new_nums=[sum(c) for c in com] #각각의 순열을 int형으로 변환
    res=list(set(new_nums))

    for i in range(len(res)):
        if res[i]!=(i+1):
            return (i+1)
            break
        

print(solution(n,nums))
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

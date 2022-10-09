# https://velog.io/@yujng/%EB%B0%B1%EC%A4%80-5639%EB%B2%88%EC%9D%B4%EC%A7%84-%EA%B2%80%EC%83%89-%ED%8A%B8%EB%A6%AC-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython

import sys
sys.setrecursionlimit(10**9)
nums = []
while True:                            
    try:
        nums.append(int(sys.stdin.readline()))
    except:
        break
        
def postorder(s, e):
    if s > e:
        return
    mid = e + 1                         # 오른쪽 노드가 없을 경우

    for i in range(s+1, e+1):
        if nums[s] < nums[i]:
            mid = i
            break

    postorder(s+1, mid-1)               # 왼쪽 확인
    postorder(mid, e)                   # 오른쪽 확인
    print(nums[s])

postorder(0, len(nums)-1)
import sys
from typing import Sequence
sys.setrecursionlimit(100000)
input = sys.stdin.readline
def get_post_order(nums:Sequence) -> Sequence:
    length = len(nums)      # nums의 길이 저장
    if length <= 1:         # nums가 leaf면 바로 반환
        # return
        return nums
    for i in range(1, length):  # 1부터 시작하는 이유: 0은 root이기 때문에 후위 순회에서는 마지막에 출력이라 빼줌.
        if nums[i] > nums[0]:   # 오른쪽 서브트리인 경우를 찾으면 분리 시킴
            return get_post_order(nums[1:i]) + get_post_order(nums[i:]) + [nums[0]]
    # 여기는 이제 오른쪽 서브트리가 없는 경우에는 왼쪽 서브트리만 보내면 되서.
    return get_post_order(nums[1:]) + [nums[0]]
if __name__ == '__main__':
    nums = []
    while True:
        try:
            nums.append(int(input()))
        except:
            break
    nums = get_post_order(nums)
    for n in nums:
        print(n)
# 한 패스에서 마지막 교환이 일어난 곳을 기준으로
# 다음패스에서는 해당 교환지점까지만 수행

from typing import MutableSequence

a=[1,3,9,4,7,8,6]
# a = [9, 1, 3, 4, 6, 7, 8]  # 셰이커정렬
cnt = 0
flag = 0

def bubble_sort(a: MutableSequence) -> None:
    global cnt, flag
    n = len(a)  # n=7
    for i in range(n-1):  # ** i =0,1,2,3,4,5 즉 n-1인 6번 반복됨
        ex = 0  # 이번 패스에서 교환횟수 초기화
        for j in range(n-1, flag, -1):  # j =
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                ex += 1  # 교환회수 찾기
                flag = j
            cnt += 1
            print(a)
        if ex == 0:
            break


bubble_sort(a)

print(a)
print(cnt)

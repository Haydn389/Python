# 이미 정렬이 완료 된 경우 더이상 수행안하도록

from typing import MutableSequence

# a=[6,4,3,7,1,9,8]
a=[9,1,3,4,6,7,8] #셰이커정렬
# a = [1, 3, 4, 6, 7, 8, 9]
cnt = 0

def bubble_sort(a: MutableSequence) -> None:
    global cnt
    n = len(a)  # n=7
    for i in range(n-1):  # ** i =0,1,2,3,4,5 즉 n-1인 6번 반복됨
        ex = 0 #이번 패스에서 교환횟수 초기화
        for j in range(n-1, i, -1):  # j =
            cnt += 1
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                ex += 1 #교환회수 찾기
        if ex == 0:break #이번 패스에서 교환횟수가 0이라면 이후 패스에서도 교환할 필요없으니 여기서 종료

bubble_sort(a)

print(a)
print(cnt)

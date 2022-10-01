# [Do it! 실습 6-5] 셰이커 정렬 알고리즘 구현하기(정렬 과정을 출력)

from typing import MutableSequence

def shaker_sort_verbose(a: MutableSequence) -> None:
    """"셰이커 정렬(정렬 과정을 출력)"""
    ccnt = 0  # 비교 횟수
    scnt = 0  # 교환 횟수
    left = 0
    n = len(a)
    right = len(a) - 1
    last = right
    i = 0
    while left < right:
        print(f'패스>{i}')
        i += 1
        for j in range(right, left, -1):
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        left = last

        if (left == right):
             break
        print(f'패스>>{i}')
        i += 1
        for j in range(left, right):
            ccnt += 1
            if a[j] > a[j + 1]:
                scnt += 1
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j
        right = last
    print(f'비교를 {ccnt}번 했습니다.')
    print(f'교환을 {scnt}번 했습니다.')

if __name__ == '__main__':
    # print('셰이커 정렬을 수행합니다.')
    # num = int(input('원소 수를 입력하세요.: '))
    # x = [None] * num  # 원소 수 num인 배열을 생성

    # for i in range(num):
    #     x[i] = int(input(f'x[{i}] : '))
    x = [9, 1, 3, 4, 6, 7, 8]  # 셰이커정렬
    shaker_sort_verbose(x)  # 배열 x를 단순 교환 정렬

    # print('오름차순으로 정렬했습니다.')
    # for i in range(num):
    #     print(f'x[{i}] = {x[i]}')
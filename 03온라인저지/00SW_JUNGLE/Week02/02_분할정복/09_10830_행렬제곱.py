# https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-10830-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%96%89%EB%A0%AC-%EC%A0%9C%EA%B3%B1-%EA%B3%A8%EB%93%9C4-%EB%B6%84%ED%95%A0-%EC%A0%95%EB%B3%B5
import sys
input = sys.stdin.readline
n, b = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]
# print(n,b)
# print(arr)
# key point 1) 행렬 계산하는 과정 외워서 활용하기
# key point 2) 재귀함수 호출 후 반환값을 temp에 저장하여 활용
# key point 3) 행렬 계산하는 함수를 따로 만들기
# key point 4) 홀수와 짝수일때를나눠서 계산


def multi(arr1, arr2):  # key point) 행렬 곱하는 함수를 따로 생성한다
    # global n
    n = len(arr1)
    new_arr = [[0]*n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            cal = 0
            for i in range(n):
                cal += arr1[row][i]*arr2[i][col]
            new_arr[row][col] = cal % 1000
    return new_arr


def sol(arr, b):
    global n
    # n = len(arr)
    if b == 1:
        for i in range(n):
            for j in range(n):
                arr[i][j] %= 1000
        return arr

    temp = sol(arr, b//2)

    if b % 2 == 0:
        return multi(temp, temp)
    else:
        return multi(multi(temp, temp), arr)

result = sol(arr, b)

for res in result:
    print(*res)

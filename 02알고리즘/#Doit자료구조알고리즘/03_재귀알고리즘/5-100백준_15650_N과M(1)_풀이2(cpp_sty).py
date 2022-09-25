# 백트래킹 연습(순열)
# nPm : 서로 다른 n개중에 r개를 선택하는 경우의 수를 의미합니다. (순서 상관 있음)
import sys
n, m = map(int, sys.stdin.readline().split())
# 1부터 N까지 자연수 중에서 중복없이 M 개를 고른 (길이가 M인)수열
# i : 트리의 깊이(N-Queen에서는 열 번호, m과 관련)
# j : 입력되는 값(N-Queen에서는 행 번호, n과 관련)
cnt = 0
pos = [0] * (m)
flag_c = [False] * (n)
def n_queens(i):
    # 풀이1과 다르게 m-1이 아니고 m인 이유: 풀이1은 함수 진입 전 depth검사를 하지만 풀이2는 인단 함수 진입 해보고 나서 depth 검사를 한다.
    if i == m:
        # (depth 검사란 m의 길이 만큼 도달했는지 여부 판단)
        global cnt
        cnt += 1
        for k in range(m):
            print(pos[k], end=" ")
        print()
        return
    for j in range(n):
        if flag_c[j] == False:
            pos[i] = j
            flag_c[j] = True
            n_queens(i+1)
            flag_c[j] = False


n_queens(0)
print(cnt)

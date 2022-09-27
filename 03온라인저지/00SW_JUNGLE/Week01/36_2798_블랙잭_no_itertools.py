# 백트래킹 연습(조합)
# nCm : 서로 다른 n개중에 r개를 선택하는 경우의 수를 의미합니다. (순서 상관 없음)
import sys
n, max_val = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
cnt = 0
pos = [0] * (3)
flag_c = [False] * (n)
ans = 0
def n_queens(i, cut):
    if i == 3:
        global cnt, ans
        cnt += 1
        s = 0
        for k in range(3):
            s += a[pos[k]]
        if s > ans and s <= max_val:
            ans = s
        return

    for j in range(n):
        if (flag_c[j] == False) and (cut <= j):
            pos[i] = j
            flag_c[j] = True
            n_queens(i+1, j)
            flag_c[j] = False

n_queens(0, 0)
print(ans)


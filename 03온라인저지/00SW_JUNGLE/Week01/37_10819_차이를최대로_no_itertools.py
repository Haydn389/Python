# 백트래킹 연습(조합)
# nCm : 서로 다른 n개중에 r개를 선택하는 경우의 수를 의미합니다. (순서 상관 없음)
import sys
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))
cnt = 0
pos = [0] * (n)
flag_c = [False] * (n)
ans = 0

def n_queens(i):
    if i == n:
        global cnt, ans
        cnt += 1
        s = 0
        A = []
        for k in range(n):
            A.append(a[pos[k]])
            # print(pos[k], end=" ")
        for i in range(n-1):
            s += abs(A[i]-A[i+1])
        if s > ans:
            ans = s
        return

    for j in range(n):
        if (flag_c[j] == False):
            pos[i] = j
            flag_c[j] = True
            n_queens(i+1)
            flag_c[j] = False


n_queens(0)
print(ans)

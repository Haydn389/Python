#백트래킹 연습(중복순열)
#n π m : 중복 가능한 n개중에서 r개를 선택하는 경우의 수를 의미합니다. (순서 상관 있음)
import sys
n, m = map(int, sys.stdin.readline().split())
# i : 트리의 깊이(N-Queen에서는 열 번호, m과 관련)
# j : 입력되는 값(N-Queen에서는 행 번호, n과 관련)

cnt = 0
pos = [0] * (m)
flag_c = [False] * (n)

def n_queens(i):
    if i == m:
        global cnt
        cnt += 1
        for k in range(m):
            # print(pos[k]+1, end=" ")
            print(*pos)
        print()
        return
    for j in range(n):
    # if (flag_c[j] == False) and (cut <= j): 
        pos[i] = j
        # flag_c[j] = True
        n_queens(i+1)
        # flag_c[j] = False


n_queens(0)
print(cnt)

#백트래킹 연습(조합)
#nCm : 서로 다른 n개중에 r개를 선택하는 경우의 수를 의미합니다. (순서 상관 없음)

import sys
n, m = map(int, sys.stdin.readline().split())
cnt = 0
pos = [0] * (m)
flag_c = [False] * (n)

def n_queens(i, cut):
    if i == m:
        global cnt
        cnt += 1
        for k in range(m):
            print(pos[k], end=" ")
        print()
        return
    for j in range(n):
        if (flag_c[j] == False) and (cut <= j): 
            #cut : 이전단계에서 넘어온 j값을 가지고 있음, 
            # N과M 풀이(1)과 비교해보시길 n,m=4,3 넣고 step 68 부터~보면 딱 80스텝에서 차이발생!!
            #즉, (cut<=j)는 현재 j가 이전단계의 j 이상일때만 수행됨
            #이후 step82와 step99가 다시 동일한 단계가 됨
            pos[i] = j
            flag_c[j] = True
            n_queens(i+1, j)
            flag_c[j] = False


n_queens(0, 0)
print(cnt)

import sys

N = int(sys.stdin.readline().strip())

ans = 0
pos= [0 for _ in range(N)]
flag_c = [False for _ in range(N)]
flag_ld = [False for _ in range(N*2-1)]
flag_rd = [False for _ in range(N*2-1)]
def n_queens(r):
    if r == N:
        global ans
        ans += 1
        return 
    for i in range(N):
        if flag_c[i] == False and flag_ld[r+i] == False and flag_rd[i-r+(N-1)]==False:
            pos[r] = i
            flag_c[i] = flag_ld[r+i] = flag_rd[i-r+(N-1)] = True
            n_queens(r+1)
            flag_c[i] = flag_ld[r+i] = flag_rd[i-r+(N-1)] = False
n_queens(0)
print(ans)
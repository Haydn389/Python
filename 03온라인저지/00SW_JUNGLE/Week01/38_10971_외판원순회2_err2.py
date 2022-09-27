import sys
sys.setrecursionlimit(10**8)  # 10^8 까지 늘림.
m = n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
pos = [0]*m
flag = [False]*n
ans = 1e9

def set(i):
    global ans
    if i == m:
        s = 0
        for k in range(n):
            s += data[pos[k % n]][pos[(k+1) % n]]
        if s < ans:
            ans = s
    else:
        for j in range(n):
            if flag[j] == False:
                pos[i] = j
                flag[j] = True
                set(i+1)
                flag[j] = False
set(0)
print(ans)

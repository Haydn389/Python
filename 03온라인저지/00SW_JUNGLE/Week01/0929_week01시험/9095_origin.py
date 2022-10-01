import sys
sys.setrecursionlimit(10**8)  # 10^8 까지 늘림
t=int(sys.stdin.readline())
def solve(i):
    if i==1:
        return 1 
    elif i==2:
        return 2
    elif i==3:
        return 4
    else:
        return solve(i-1)+solve(i-2)+solve(i-3)
for _ in range(t):
    x=int(sys.stdin.readline())
    print(solve(x))
import sys
sys.setrecursionlimit(10**8)  # 10^8 까지 늘림
t=int(sys.stdin.readline()) 
def solve(i):
    if i<=2:    #i==1 일때 1반환, i==2일때 2반환
        return i 
    elif i==3:  #i==3 일때 4반환
        return 4
    else:
        return solve(i-1)+solve(i-2)+solve(i-3)
for _ in range(t):
    x=int(sys.stdin.readline())
    print(solve(x))
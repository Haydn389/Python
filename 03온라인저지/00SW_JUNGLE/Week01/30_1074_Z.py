import sys
# n = 2
n, r,c=map(int,sys.stdin.readline().split())
# r, c = 3, 1


# 01 주어진 N에 대하여 1,2,3,4구역으로 나누어 어디구역에 속해있는지 판단.

def sol(n, r, c, cnt):
    #크기가 0이 되었을때 현재까지 쌓아둔 cnt 를 반환 
    if n == 0:
        return cnt
    half = 2**(n-1)
    if r < half and c < half:  # 1구역
        div = 1
    elif r < half and c >= half:  # 2구역
        div = 2
        c-=half
    elif r >= half and c < half:  # 3구역
        div = 3
        r-=half
    else:  # 4구역
        div = 4
        r-=half
        c-=half
    cnt+=(div-1)*half**2
    return (sol(n-1, r, c, cnt))

print(sol(n, r, c, 0))

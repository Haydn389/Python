import sys
sys.setrecursionlimit(10**7)
n, r, c = map(int, sys.stdin.readline().split())
cnt = 0
def z(n, r, c):
    global cnt
    if n == 0:
        return
    half = 2**(n-1)
    if r < half and c < half:
        div = 1
    elif r < half and c >= half:
        div = 2
        c -= half
    elif r >= half and c < half:
        div = 3
        r -= half
    else:
        div = 4
        r -= half
        c -= half
    cnt += (div-1)*half**2
    return z(n-1, r, c)


z(n, r, c)
print(cnt)

import sys
input = sys.stdin.readline

n = int(input())
a = [input().strip() for _ in range(n)]


def cut(x, y, s):
    cnt = 0
    for i in range(y, y+s):
        for j in range(x, x+s):
            cnt += int(a[i][j])
    if cnt == 0:
        return "0"
    elif cnt == s**2:
        return "1"
    else:
        h = s//2
        return "("+cut(x, y, h)+cut(x+h, y, h)+cut(x, y+h, h)+cut(x+h, y+h, h)+")"


print(cut(0, 0, n))

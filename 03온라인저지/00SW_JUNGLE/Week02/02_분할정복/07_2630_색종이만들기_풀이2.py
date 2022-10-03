# https://zidarn87.tistory.com/378
import sys
n = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
white = blue = 0

def div(x, y, n):
    global white, blue
    color = a[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != a[i][j]:
                hf = n//2
                div(x, y, hf)
                div(x, y+hf, hf)
                div(x+hf, y, hf)
                div(x+hf, y+hf, hf)
                return
    if color == 0:
        white += 1
    else:
        blue += 1
div(0, 0, n)
print(white)
print(blue)

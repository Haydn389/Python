import sys
input=sys.stdin.readline

n=int(input())
a=[["*"]*n for _ in range(n)]
# for x in a:
#     print("".join(x))

def zero(x,y,n):
    for i in range(x,x+n):
        for j in range(y,y+n):
            a[i][j]=" "

def solve(x,y,n):
    for i in range(x,x+n):
        for j in range(y,y+n):
            half=n//3
            solve(x,y,half)
            solve(x,y+half,half)
            solve(x,y+half*2,half)
            solve(x+half,y,half)
            zero(x+half,y+half,half)
            solve(x+half,y+half*2,half)
            solve(x+half*2,y,half)
            solve(x+half*2,y+half,half)
            solve(x+half*2,y+half*2,half)
            return

solve(0,0,n)
for x in a:
    print("".join(x))

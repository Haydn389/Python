import sys
input=sys.stdin.readline

n=int(input())

a=[list(map(int,list(input().rstrip()))) for _ in range(n)]

def solve(x,y,n):
    for i in range(x,x+n):
        for j in range(y,y+n):
            if a[x][y]!=a[i][j]:
                half=n//2
                print("(",end="")
                solve(x,y,half)
                solve(x,y+half,half)
                solve(x+half,y,half)
                solve(x+half,y+half,half)
                print(")",end="")
                return
    print(a[x][y],end="")

solve(0,0,n)
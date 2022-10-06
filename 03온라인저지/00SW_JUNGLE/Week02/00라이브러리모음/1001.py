import sys
input=sys.stdin.readline

n=int(input())

a=[list(input().rstrip()) for _ in range(n)]

print(a)
def div(x,y,n):
    flag=a[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if flag!=a[i][j]:
                half=n//2
                print("(",end="")
                div(x,y,half)
                div(x,y+half,half)
                div(x+half,y,half)
                div(x+half,y+half,half)
                print(")",end="")
                return
    print(flag,end="")
div(0,0,n)
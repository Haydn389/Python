import sys
input=sys.stdin.readline
# sys.setrecursionlimit(10**8) # 10^8 까지 늘림.

n= int(input())
a=[]
# for _ in range(n):
#     a.append(list(input().rstrip()))
a= [list(input().rstrip()) for _ in range(n)]

print(a)

def div(x,y,n):
    flag=a[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if flag!=a[i][j]:
                print("(",end="")
                half=n//2
                div(x,y,half)
                div(x,y+half,half)
                div(x+half,y,half)
                div(x+half,y+half,half)
                print(")",end="")
                return
    print(flag,end="")




div(0,0,n)
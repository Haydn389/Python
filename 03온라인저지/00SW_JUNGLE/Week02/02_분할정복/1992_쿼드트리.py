import sys
input=sys.stdin.readline

n=int(input())
a=[]
for _ in range(n):
    a.append(list(map(int,list(input().rstrip()))))
# print(n,a)
# print(a[0][0])
# white,blue=0,0

def div(x,y,n):
    flag =a[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if a[i][j]!=flag:
                hf=n//2
                print("(",end="")
                div(x,y,hf)
                div(x,y+hf,hf)
                div(x+hf,y,hf)
                div(x+hf,y+hf,hf)
                print(")",end="")
                return
    print(flag,end="")

div(0,0,n)
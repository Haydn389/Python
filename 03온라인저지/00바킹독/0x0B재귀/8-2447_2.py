import sys
input=sys.stdin.readline

n=int(input())
a=[[" "]*n for _ in range(n)]
# for x in a:
#     print("".join(x))

def zero(x,y,n):
    for i in range(x,x+n):
        for j in range(y,y+n):
            a[i][j]=" "

#a[x][x] 부터 a[x+n-1][y+n-1] 까지 규칙에 맞게 "*"를 넣는 함수
def solve(x,y,n):
    print(f"x:{x},y:{y},n:{n}")
    if n==1:
        a[x][y]="*"
        for x in a:
            print("".join(x))
        print("-"*50)
        return
    for i in range(0,3):
        for j in range(0,3):
            if (i==1 and j==1):
                continue
            solve(x+n//3*i,y+n//3*j,n//3)
solve(0,0,n)
for x in a:
    print("".join(x))

import sys
input=sys.stdin.readline

n=int(input())

a=[list(map(int,input().split())) for _ in range(n)]
res=[0,0]

#한변이n인 정사각형의 색을 판단하여 카운트 하는 함수
def solve(x,y,n):
    for i in range(x,x+n):
        for j in range(y,y+n):
            #n^2의 원소중 하나라도 일치하지 않는원소가 있는경우 재귀적으로 분할
            if a[x][y]!=a[i][j]:
                half=n//2
                solve(x,y,half)
                solve(x,y+half,half)
                solve(x+half,y,half)
                solve(x+half,y+half,half)
                return #분할된 작은 사각형들에 대해 모두 완료되면 return
    res[a[x][y]]+=1
solve(0,0,n)

for i in res:
    print(i)
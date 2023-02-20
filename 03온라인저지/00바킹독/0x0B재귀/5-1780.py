import sys
input=sys.stdin.readline

n=int(input())

a=[list(map(int,input().split())) for _ in range(n)]
res=[0,0,0]

def func(x,y,n):
    for i in range(x,x+n):
        for j in range(y,y+n):
            if a[x][y]!=a[i][j]:
                temp=n//3
                func(x,y,temp)
                func(x,y+temp,temp)
                func(x,y+temp*2,temp)
                func(x+temp,y+0,temp)
                func(x+temp,y+temp,temp)
                func(x+temp,y+temp*2,temp)
                func(x+temp*2,y+0,temp)
                func(x+temp*2,y+temp,temp)
                func(x+temp*2,y+temp*2,temp)
                return 
    res[a[x][y]+1]+=1
    return
    
func(0,0,n)
for i in res:
    print(i)
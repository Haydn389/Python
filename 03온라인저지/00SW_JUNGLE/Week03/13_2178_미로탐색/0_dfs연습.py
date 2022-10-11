import sys
sys.setrecursionlimit(10**5)
input=sys.stdin.readline

n,m=map(int,input().split())

a=[list(input().rstrip()) for _ in range(n)]

def dfs(x,y):
    if x<0 or y<0 or x>=n or y>=m or a[x][y]!='0':
        return
    a[x][y]='1'
    dfs(x+1,y)
    dfs(x,y+1)
    dfs(x-1,y)
    dfs(x,y-1)

print(a)
# print(a[0][0])
cnt=0
for i in range(n):
    for j in range(m):
        if a[i][j]=='0':
            dfs(i,j)
            cnt+=1
            print("*"*50)
            for k in a:
                print(*k)
print(cnt)
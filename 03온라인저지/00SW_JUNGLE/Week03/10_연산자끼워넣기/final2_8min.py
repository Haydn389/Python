import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

n=int(input())
num=list(map(int, input().split()))
add,sub,mul,div=map(int, input().split())

def dfs(i,res,add,sub,mul,div):
    global max_val,min_val
    if i==n:
        max_val=max(res,max_val)
        min_val=min(res,min_val)
        return
    if add>0:
        dfs(i+1,res+num[i],add-1,sub,mul,div)
    if sub>0:
        dfs(i+1,res-num[i],add,sub-1,mul,div)
    if mul>0:
        dfs(i+1,res*num[i],add,sub,mul-1,div)
    if div>0:
        dfs(i+1,int(res/num[i]),add,sub,mul,div-1)

max_val=-1e12
min_val=1e12

dfs(1,num[0],add,sub,mul,div)
print(max_val)
print(min_val)
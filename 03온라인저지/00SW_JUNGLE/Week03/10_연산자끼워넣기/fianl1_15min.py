import sys
input=sys.stdin.readline

n=int(input())
nums=list(map(int,input().split()))
add,sub,mul,div=map(int,input().split())

def dfs(i,res):
    global add,sub,mul,div,max_val,min_val
    if i==n-1:
        max_val=max(max_val,res)
        min_val=min(min_val,res)
        return
    if add>0:
        add-=1
        dfs(i+1,res+nums[i+1])
        add+=1
    if sub>0:
        sub-=1
        dfs(i+1,res-nums[i+1])
        sub+=1
    if mul>0:
        mul-=1
        dfs(i+1,res*nums[i+1])
        mul+=1
    if div>0:
        div-=1
        dfs(i+1,int(res/nums[i+1]))
        div+=1

max_val=-1e9
min_val=1e9

dfs(0,nums[0])

print(max_val)
print(min_val)
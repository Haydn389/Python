import sys
input=sys.stdin.readline
m=int(input())
data=list(map(int,input().split()))
add,sub,mul,div=map(int,input().split())

min_val=1e9
max_val=-1e9

def dfs(i,now):
    global min_val,max_val,add,sub,mul,div
    if i==m:
        max_val=max(now,max_val)
        min_val=min(now,min_val)
    else:
        if add>0:
            add-=1
            dfs(i+1,now+data[i])
            add+=1
        if sub>0:
            sub-=1
            dfs(i+1,now-data[i])
            sub+=1
        if mul>0:
            mul-=1
            dfs(i+1,now*data[i])
            mul+=1
        if div>0:
            div-=1
            dfs(i+1,now//data[i])
            div+=1

dfs(1,data[0])
print(max_val)
print(min_val)
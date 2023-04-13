# 6 
# 1 2 3 4 5 6
# 2 1 1 1
import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
oper=list(map(int,input().split()))
max_val=-sys.maxsize
min_val=sys.maxsize
def dfs(i,tot,add,sub,mul,div):
    global max_val,min_val
    if i==n:
        max_val=max(max_val,tot)
        min_val=min(min_val,tot)
        return
    if add!=0:
        dfs(i+1,tot+a[i],add-1,sub,mul,div)
    if sub!=0:
        dfs(i+1,tot-a[i],add,sub-1,mul,div)
    if mul!=0:
        dfs(i+1,tot*a[i],add,sub,mul-1,div)
    if div!=0:
        dfs(i+1,int(tot/a[i]),add,sub,mul,div-1)

dfs(1,a[0],oper[0],oper[1],oper[2],oper[3])
print(max_val)
print(min_val)
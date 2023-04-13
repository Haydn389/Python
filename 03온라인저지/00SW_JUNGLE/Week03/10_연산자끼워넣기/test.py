# print(-10//3)
# print(int(-10/3))

import sys
input = sys.stdin.readline

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
        add-=1
        # tot+=a[i]
        dfs(i+1,tot+a[i],add,sub,mul,div)
        add+=1
    if sub!=0:
        sub-=1
        # tot-=a[i]
        dfs(i+1,tot-a[i],add,sub,mul,div)
        sub+=1
    if mul!=0:
        mul-=1
        # tot*=a[i]
        dfs(i+1,tot*a[i],add,sub,mul,div)
        mul+=1
    if div!=0:
        div-=1
        # tot=int(tot/a[i])
        dfs(i+1,int(tot/a[i]),add,sub,mul,div)
        div+=1

dfs(1,a[0],oper[0],oper[1],oper[2],oper[3])
print(max_val)
print(min_val)


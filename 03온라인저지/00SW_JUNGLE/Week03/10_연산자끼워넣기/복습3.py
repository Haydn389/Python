import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
add,sub,mul,div = map(int, input().split())

res=0
max_r=-1e9
min_r=1e9

def cal(i,res):
    global max_r,min_r,add,sub,mul,div
    if i==(n-1):
        max_r=max(max_r,res)
        min_r=min(min_r,res)
        return
    if add>0:
        add-=1
        cal(i+1,res+num[i+1])
        add+=1
    if sub>0:
        sub-=1
        cal(i+1,res-num[i+1])
        sub+=1
    if mul>0:
        mul-=1
        cal(i+1,num[i+1]*res)
        mul+=1
    if div>0:
        div-=1
        cal(i+1,int(res/num[i+1]))
        div+=1
    return

cal(0,num[0])

print(max_r)
print(min_r)
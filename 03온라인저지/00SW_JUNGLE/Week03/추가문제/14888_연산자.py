# 6
# 1 2 3 4 5 6
# 2 1 1 1
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

n=int(input())
a=list(map(int,input().split()))
o=list(map(int,input().split()))
pos=[]
maxValue=-1e9
minValue=1e9
def dfs(i,tot,add,sub,mul,div):
    global maxValue,minValue
    if i==n:
        maxValue=max(maxValue,tot)
        minValue=min(minValue,tot)
        return
    if add!=0:
        dfs(i+1,tot+a[i],add-1,sub,mul,div)
    if sub!=0:
        dfs(i+1,tot-a[i],add,sub-1,mul,div)
    if mul!=0:
        dfs(i+1,tot*a[i],add,sub,mul-1,div)
    if div!=0:
        dfs(i+1,int(tot/a[i]),add,sub,mul,div-1)


dfs(1,a[0],o[0],o[1],o[2],o[3])

print(maxValue)
print(minValue)
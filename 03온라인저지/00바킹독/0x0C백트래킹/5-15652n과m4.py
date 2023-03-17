#중복조합(dfs 가능)
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
pos=[0]*m
def solve(i):
    global start
    if i==m:
        print(*pos)
        return
    for j in range(start,n+1):
        pos[i]=j
        start=j
        solve(i+1)

start=1
solve(0)
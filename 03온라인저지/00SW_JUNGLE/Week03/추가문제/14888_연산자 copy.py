# 6
# 1 2 3 4 5 6
# 2 1 1 1
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

n,m=map(int,input().split()) #n개중에 m개
pos=[0]*m
maxValue=-1e9
minValue=1e9
def dfs(i):
    if i==m:
        print(pos)
        return
    for j in range(n):
        if not visited[j]:
            pos[i]=j+1
            visited[j]=True
            dfs(i+1)
            visited[j]=False

visited=[False]*(n)
dfs(0)
import sys
input = sys.stdin.readline

n,m=map(int,input().split())
pos=[0]*m
visited=[False]*(n+1)

def solve(i):
    if i==m:
        print(*pos)
        return
    for j in range(1,n+1):
        if not visited[j]:
            pos[i]=j
            visited[j]=True
            solve(i+1)
            visited[j]=False

solve(0)
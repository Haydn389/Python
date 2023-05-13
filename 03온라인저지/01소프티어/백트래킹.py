import sys
input=sys.stdin.readline

# n,m=map(int,input().split())
n,m=4,3
pos=[0]*(m)
visited=[0]*(n)


def dfs(i):
    if i==m:
        print(pos)
        return
    for j in range(1,n):
        if not visited[j]:
          pos[i]=j
          visited[j]=1
          dfs(i+1)  
          visited[j]=0
dfs(0)
import sys
n,m=map(int,sys.stdin.readline().split())

cnt=0

pos=[0]*m #자리수
arr=[] #자리수
visited=[False]*n

def dfs(i):
    global cnt
    if i ==m:
        cnt+=1
        print(pos,arr)
        return
    
    for j in range(n):
        if not visited[j]:
            pos[i]=j
            arr.append(j)
            visited[j]=True
            dfs(i+1)
            visited[j]=False
            arr.pop()

dfs(0)
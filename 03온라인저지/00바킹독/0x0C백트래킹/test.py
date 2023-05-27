
n,m=4,3
pos=[0]*m
visited=[False]*(n+1)
def back(i):
    if i==m:
        print(pos)
        return
    for j in range(n):
        if not visited[j]:
            # visited[j]=True
            pos[i]=j
            back(i+1)
            # visited[j]=False

back(0)
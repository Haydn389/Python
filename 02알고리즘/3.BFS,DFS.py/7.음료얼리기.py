import sys
n,m=map(int,sys.stdin.readline().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().strip()))) #한 줄에 입력된 원소들을 리스트화 시켜줌

def dfs(x,y):
    if (x>n-1 or y>m-1 or x<0 or y<0):
        return False
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True

    return False
# print(data)
res=0
for i in range(n):
    for j in range(m):
        if(dfs(i,j)==True):
            res+=1

print(res)
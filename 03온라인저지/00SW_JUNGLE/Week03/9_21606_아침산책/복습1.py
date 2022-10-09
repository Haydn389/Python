import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(v):
    cnt=0
    for i in graph[v]:
        if location[i]==1:
            cnt+=1
        else:
            if not visited[i]:
                visited[i]=True
                cnt+=dfs(i)
    return cnt

v=int(input())
location=[0]+list(map(int,list(input().rstrip())))
graph=[[] for _ in range(v+1)]
ans=0
for _ in range(v-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    # if location[a]==location[b]:   #***틀림!!
    if location[a]==1 and location[b]==1:
        ans+=2


visited=[False]*(v+1)
# for start in range(v+1): #***틀림!!
for start in range(1,v+1): #실외일경우만 들어감 #***틀림!!
    if not visited[start] and location[start]==0:
        visited[start]=True
        temp=dfs(start)
        ans+=temp*(temp-1)

print(ans)
    
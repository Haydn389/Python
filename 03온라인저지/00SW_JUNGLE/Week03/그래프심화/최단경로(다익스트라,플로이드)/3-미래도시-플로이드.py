import sys
input=sys.stdin.readline

n,m=map(int,input().split())
INF=sys.maxsize
graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0

for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

x,k=map(int,input().split())

for k in range(1,n+1):
    # for i in range(1,n+1):
    for i in [1]:
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

print(graph[1][k]+graph[k][x])

#1->k->x
for p in graph[1:]:
    for q in p[1:]:
        if q==INF:
            print(0,end=" ")
        else:
            print(q,end=" ")
    print()
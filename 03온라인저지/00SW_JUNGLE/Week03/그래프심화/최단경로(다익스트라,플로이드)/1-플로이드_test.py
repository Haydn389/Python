import sys
INF=sys.maxsize
input= sys.stdin.readline
n=int(input())
m=int(input())

graph=[[INF]*(n+1) for _ in range(n+1)]

#i==i인경우 0으로 채우기

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

#주어진 최소비용 입력
for _ in range(m):
    a,b,c=map(int,input().split())
    if graph[a][b]>c:
        graph[a][b]=c
    # graph[a][b]=min(c,graph[a][b])

#플-워 수행3중 for문
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            # graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])
            c=graph[a][k]+graph[k][b]
            if graph[a][b]>c:
                graph[a][b]=c

for p in graph[1:]:
    for q in p[1:]:
        if q==INF:
            print(0,end=" ")
        else:
            print(q,end=" ")
    print()
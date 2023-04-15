#인접행렬 방식
import sys
INF=sys.maxsize
input= sys.stdin.readline
n=int(input())
e=int(input())

graph=[[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

for _ in range(e):
    a,b,c=map(int,input().split())
    graph[a][b]=min(c,graph[a][b])

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

for p in graph[1:]:
    for q in p[1:]:
        if q==INF:
            print(0,end=" ")
        else:
            print(q,end=" ")
    print()
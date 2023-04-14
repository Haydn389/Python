#다익스트라 문제를 플로이드로 풀어보기
import sys
INF=sys.maxsize
from heapq import heappush,heappop

n,m=map(int,input().split())
start=int(input())


graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0


for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=c

for k in range(1,n+1):
    # for i in range(1,n+1):
    i=1
    for j in range(1,n+1):
        graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

for p in graph[1:]:
    for q in p[1:]:
        if q==INF:
            print(0,end=" ")
        else:
            print(q,end=" ")
    print()
import sys
from heapq import heappop,heappush
input=sys.stdin.readline

n,m=map(int,input().split())
start=int(input())
INF=sys.maxsize
graph=[[] for _ in range(n+1)]
dist=[INF]*(n+1)
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijk(start):
    q=[]
    dist[start]=0
    heappush(q,(0,start))

    while q:
        val,now=heappop(q)
        if dist[now]<val:
            continue
        for i in graph[now]:
            cost=i[1]+val
            if dist[i[0]]>cost:
                dist[i[0]]=cost
                heappush(q,(cost,i[0]))


dijk(start)
# print(dist)
for p in dist[1:]:
    print("INF" if p==INF else p)
import sys
from heapq import heappush,heappop
INF=sys.maxsize

n,m,start=map(int,input().split())
dist=[INF]*(n+1)
graph=[[] for _ in range(n+1)]

for _ in range(m):
    s,e,cost=map(int,input().split())
    graph[s].append((e,cost))

def dijk(start):
    q=[]
    heappush(q,(0,start))
    dist[start]=0
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
print(dist)
print(max(dist[1:]))
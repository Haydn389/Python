import sys
from heapq import heappush,heappop
import copy
input=sys.stdin.readline

n,m=map(int,input().split())
INF=sys.maxsize
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

x,k=map(int,input().split())

#한번은 1->k까지, 한번은 k->x까지
ans=0
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

dist=[INF]*(n+1)
dijk(2)
print(dist)
ans+=dist[k]

dist=[INF]*(n+1)
dijk(k)
print(dist)
ans+=dist[x]

print(ans)
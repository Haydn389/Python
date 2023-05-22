import sys
input=sys.stdin.readline
from heapq import heappush,heappop
INF=int(1e9)
n=int(input())
m=int(input())

dist=[INF]*(n+1)
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c)) #도착지, 비용

start,end=map(int,input().split())

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
print(dist[end])
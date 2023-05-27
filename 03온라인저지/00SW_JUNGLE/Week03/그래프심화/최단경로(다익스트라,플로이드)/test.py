from heapq import heappop,heappush
import sys
INF=sys.maxsize
input=sys.stdin.readline

n,m=map(int,input().split())
start=int(input())
graph=[[] for _ in range(n+1)]
dist=[INF]*(n+1)
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c)) #노드, 비용

def dijk(start):
    q=[]
    dist[start]=0
    heappush(q,(0,start))
    while q:
        val,now=heappop(q)
        if dist[now]<val:
            continue
        for i in graph[now]:
            cost=val+i[1]
            if dist[i[0]]>cost:
                dist[i[0]]=cost
                heappush(q,(cost,i[0]))

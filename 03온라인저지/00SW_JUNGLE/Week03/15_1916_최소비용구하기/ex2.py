from heapq import heapify,heappop,heappush
import sys
input=sys.stdin.readline
v=int(input())
e=int(input())

graph=[[] for _ in range(v+1)]
INF=int(1e9)
distance=[INF]*(v+1)

for _ in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
start,end=map(int,input().split())
q=[]
heappush(q,(0,start))
distance[start]=0
while q:
    dist,now=heappop(q)
    if distance[now]<dist:
        continue
    for i in graph[now]:
        cost=dist+i[1]
        if cost<distance[i[0]]:
            distance[i[0]]=cost
            heappush(q,(cost,i[0]))

print(distance[end])
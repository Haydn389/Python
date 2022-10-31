import sys
input=sys.stdin.readline
from collections import deque
from heapq import heappop,heappush

v,e=map(int,input().split())

graph=[[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
start,end=map(int,input().split())
INF=int(1e9) #큰 무게로 초기화
distance=[INF]*(v+1)
visitied=[False]*(v+1)
def ds(start):
    q=[]
    heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heappop(q)
        # print(">>",distance)
        if dist>distance[now]:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heappush(q,(cost,i[0]))


ds(start)
print(distance)
print(distance[end])


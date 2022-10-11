from heapq import heappop,heappush  #다익스트라는 
import sys
input=sys.stdin.readline
INF=int(1e9)

v=int(input())
e=int(input())
graph=[[] for _ in range(v+1)]
for _ in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((b,c)) #도착노드 , 비용 순으로 업데이트
start,end=map(int,input().split())

distance=[INF]*(v+1)

# print(v,e,start,end)
# print(graph)

def ds(satrt):
    q=[]
    heappush(q,(0,start))
    distance[start]=0

    while q:
        dist,now=heappop(q)
        if dist>distance[now]:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heappush(q,(cost,i[0]))

ds(start)

print(distance[end])
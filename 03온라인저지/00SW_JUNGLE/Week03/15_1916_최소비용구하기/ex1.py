from heapq import heappop,heappush
import sys
input=sys.stdin.readline
INF=int(1e9)

v=int(input())
e=int(input())
graph=[[] for _ in range(v+1)]
distance=[INF]*(v+1)
for _ in range(e):  #!** 힙에 넣어야 하나? 그냥 리스트에 넣어야하나? --> 그냥리스트
    a,b,c=map(int,input().split())
    graph[a].append((b,c)) #노드정보, 비용을 차례로 입력

start,end=map(int,input().split())

def ds(start):
    q=[]
    heappush(q,(0,start))
    while q:
        dist,now=heappop(q)
        #방문 노드 확인
        if distance[now]<dist: #!**어떤값과 어떤값을 비교해야 할까? 
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heappush(q,(cost,i[0]))

ds(start)


print(distance[end])
from heapq import heapify,heappop,heappush
import sys
input=sys.stdin.readline

v,e=map(int,input().split())
start=int(input())
graph=[[] for _ in range(v+1)]
for _ in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((b,c)) #도착노드 , 비용 순으로 업데이트
INF=int(1e9)

distance=[INF]*(v+1)


def ds(start):
    #시작노드 거리 0으로 초기화
    #힙에 넣기
    q=[]
    heappush(q,(0,start)) #거리가 앞쪽으로 와서 거리를 기준으로 힙정렬 되도록
    distance[start]=0
    while q:
        dist,now=heappop(q)
        #이미 방문했던 노드에대한 처리
        #이미 방문을 완료했으면 꺼낸원소(거리,노드)의 노드에서의 거리가 distance[now]보다 클 수 밖에없음
        if dist>distance[now]:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heappush(q,(cost,i[0]))


ds(start)

for i in range(1,v+1):
    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])
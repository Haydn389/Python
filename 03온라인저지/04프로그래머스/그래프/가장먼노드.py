#다익스트라로 풀어보자
from heapq import heappush,heappop
INF=int(1e9)

def solution(n, edge):
    m=len(edge)
    graph=[[] for _ in range(n+1)]
    for a,b in edge:
        graph[a].append((b,1))
        graph[b].append((a,1))
    dist=[INF]*(n+1)
    # print(graph)
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
    
    dijk(1)
    print(dist)    
    answer = dist.count(max(dist[1:]))
    return answer
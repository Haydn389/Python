import sys
input= sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
start= int(input())
graph=[[] for i in range(n+1)]

visited=[False]*(n+1)

dist=[INF]*(n+1)

for _ in range(m):
    a,b,c,=map(int,input().split())
    graph[a].append((b,c))

#방문하지 않은 노드 중에서 최단거리가 짧은 노드으의 번호 반환
def get_smallest_node():
    min_val=INF
    index=0
    for i in range(1, n+1):
        if dist[i] < min_val and not visited[i]:
            min_val = dist[i]
            index=i
    return index

def dijkstra(start):
    #시작노드 방문처리 및 거리 초기화
    dist[start]=0
    visited[start]=True
    for j in graph[start]:
        dist[j[0]]=j[1]
    #시작노드 제외 전체 n-1개 ㅗㄴ드에 대해 반복
    for _ in range(n-1):
        #현재 최단 거리가 가장 짧은 노드 찾아서 방문처리
        now = get_smallest_node()
        visited[now]=True
        #현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost=dist[now]+j[1]
            if dist[j[0]]>cost:
                dist[j[0]]=cost
dijkstra(start)

for i in range(1,n+1):
    if dist[i]==INF:
        print("INF")
    else:
        print(dist[i])
        
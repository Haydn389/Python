import sys
input=sys.stdin.readline

v,e=map(int,input().split())
start=int(input())
graph=[[] for _ in range(v+1)]
for _ in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
INF=int(1e9)
distance=[INF]*(v+1)
visited=[False]*(v+1)

def get_node():
    min_val=INF
    for i in range(1,v+1):
        if not visited[i] and distance[i]<min_val:
            min_val=distance[i]
            index=i
    return index

def ds(start):
    #시작노드 방문처리
    #시작노드 거리0으로 초기화
    #시작노드 인접노드 비용 수정
    visited[start]=True
    distance[start]=0
    for i in graph[start]:
        distance[i[0]]=i[1]

    #시작노드 제외 v-1회 반복
    for _ in range(v-1):
        now=get_node()
        visited[now]=True
        for j in graph[now]:
            cost=distance[now]+j[1]
            if cost<distance[j[0]]:
                distance[j[0]]=cost

ds(start)

for i in range(1,v+1):
    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])
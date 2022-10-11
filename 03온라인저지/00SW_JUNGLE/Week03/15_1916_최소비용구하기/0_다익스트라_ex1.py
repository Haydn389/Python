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
    visited[start]=True
    distance[start]=0
    for i in graph[start]:
        distance[i[0]]=i[1]

    for _ in range(v-1):  #********!! v-1회 반복
        now=get_node()
        visited[now]=True
        for j in graph[now]:
            cost=distance[now]+j[1] #********!! 현재노드까지의 거리 + 다음노드까지 거리
            if cost <distance[j[0]]: #********!! 기존 저장된 다음노드까지거리
                distance[j[0]]=cost

ds(start)

for i in range(1,v+1):
    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])
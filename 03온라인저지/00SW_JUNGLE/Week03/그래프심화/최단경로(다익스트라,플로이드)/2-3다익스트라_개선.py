from heapq import heappush,heappop
import sys
input=sys.stdin.readline

INF=sys.maxsize
n,m=map(int,input().split())
start=int(input())

graph=[[] for i in range(n+1)]
dist=[INF]*(n+1) #거리 표시

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijk(start):
    q=[]
    #시작노드 큐에 삽입
    heappush(q,(0,start))
    dist[start]=0   #***!!!주의!!!
    while q:#큐가 비어있지 않은동안
        val,now=heappop(q)
        #꺼냈는데 저장된 거리보다 작으면 continue
        if dist[now]<val:
            continue

        #현재 노드와 연결된 다른 인접노드 확인
        for i in graph[now]:
            cost=val+i[1]#***!!!주의 그래프에서는 뒤에가 비용!!!
            if dist[i[0]]>cost: #새로 계산한 비용이 작으면,
                dist[i[0]]=cost #갱신
                heappush(q,(cost,i[0])) #저장
                #***!!!주의!!!
dijk(start)

for i in range(1,n+1):
    if dist[i]==INF:
        print("INFINITY")
    else:
        print(dist[i])
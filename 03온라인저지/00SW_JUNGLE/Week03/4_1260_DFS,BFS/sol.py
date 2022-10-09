from collections import deque
import sys
input=sys.stdin.readline

def dfs(graph,v,visited):
    visited[v]=True
    print(v,end=" ")             #dfs는 함수가 호출되었을때 **방문처리** 및 @@출력@@
    # for i in sorted(graph[v]):
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True         #먼저 시작노드에 대해서만 따로 "큐에 노드를 담는순간" **방문처리** 1회 수행 
    while queue:
        v=queue.popleft()       #큐에서 pop하면서 @@출력@@
        print(v,end=" ")
        # for i in sorted(graph[v]):
        for i in graph[v]:      
            if not visited[i]:
                queue.append(i) #다른 노드 역시 큐에 노드를 담는순간 **방문처리**
                visited[i]=True

if __name__=="__main__":
    v,e,start=map(int,input().split())
    # graph = {i: [] for i in range(1, v+1)}
    graph = [[] for _ in range(v+1)] #메모리가 약간 더 적음
    for _ in range(e):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1,v+1):
        graph[i].sort()

    # print(graph)
    visited=[False]*(v+1)
    dfs(graph,start,visited)
    print()
    visited=[False]*(v+1)
    bfs(graph,start,visited) #-->graph안넘겨줘도 됨, 그래프 내부 값들에 접근할 때는 global키워드 필요x
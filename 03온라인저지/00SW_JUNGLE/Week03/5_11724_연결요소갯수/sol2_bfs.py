import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

#1) dfs/bfs는 시작노드로부터 연결된 모든 노드를 빠짐없이 탐색하고 돌아옴
#2) 따라서 
if __name__ == "__main__":
    res=0
    v,e=map(int,input().split())
    graph = [[] for _ in range(v+1)] #메모리가 약간 더 적음
    start=0
    for _ in range(e):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited=[False]*(v+1)
    cnt=0
    for i in range(1,v+1):
        if not visited[i]:
            cnt+=1
            bfs(i)
    print(cnt)
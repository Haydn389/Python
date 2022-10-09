import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(v):
    # visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            visited[i] = v
            dfs(i)

v = int(input())

graph = [[] for _ in range(v+1)]
for _ in range(v-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False]*(v+1)
visited[1]=True
# 최적화 과정1) parent 리스트를 따로만들지 않고 visited에 자신의 부모노드를 저장하면서 방문여부를 판단
# 최적호 과정2) visited = [False]*(v+1) #-->이렇게 해도 되긴 됨, 다만 1의 첫번째 노드인 6이 루트노드가 되어버림(visualizer돌려보기)
dfs(1)
for i in visited[2:]:
    print(i)

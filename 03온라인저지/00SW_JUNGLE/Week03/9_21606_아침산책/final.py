import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
def dfs(v,cnt):
    visited[v] = True  # !****방문처리
    for i in graph[v]:
        if location[i] == 1:
            cnt += 1
            # return #!***여기서 리턴하면 다른 인접 실내노드 검사를 못함
        else:
            if not visited[i]: #다른 실외노드에 방문한 적없을때
                cnt = dfs(i,cnt)
    return cnt

ans = 0
v = int(input())
location = [0]+list(map(int, list(input().rstrip())))

graph = [[] for _ in range(v+1)]

for _ in range(v-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    if location[a] == 1 and location[b] == 1:
        ans += 2


visited = [False]*(v+1)
for start in range(1, v+1):
    # if not visited[start] and location[start]==0:
    if location[start] == 0 and not visited[start]:
        temp = dfs(start,0)
        ans += temp*(temp-1)

print(ans)

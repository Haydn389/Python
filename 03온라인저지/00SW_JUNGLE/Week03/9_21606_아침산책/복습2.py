import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)    #***틀림! dfs에서는 재귀 깊이를 늘려주자!!
def dfs(v, cnt):
    visited[v] = True
    for i in graph[v]:
        if location[i] == 1:  # 1)실내노드일때
            cnt += 1
            # return            #***틀림! 여기서 retrun 해버리면 v의 연결노드인 i노드중 한번이라도 실내나오면 빠져나가버림
        else:
            if not visited[i]:  # 2) 실외노드이지만 방문한적 없을때
                cnt = dfs(i, cnt)
    return cnt

ans = 0
v = int(input())
location = [None]+list(map(int, list(input().rstrip())))

graph = [[] for _ in range(v+1)]

for _ in range(v-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    if location[a] == 1 and location[b] == 1:
        ans += 2



visited = [False]*(v+1)
for start in range(1, v+1):
    # 실외노드일경우 and 방문한 적 없을때 방문
    if location[start] == 0 and not visited[start]:
        temp = dfs(start, 0)
        ans += temp*(temp-1)
print(ans)

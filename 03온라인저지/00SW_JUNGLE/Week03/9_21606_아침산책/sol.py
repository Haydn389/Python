import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def dfs(v, cnt):
    visited[v] = True  # 노드 방문처리
    for i in graph[v]:  # 해당 노드와 인접한 노드를 차례로 순회
        if location[i] == 1:  # 1) 인접노드가 실내인 경우만 cnt+=1
            cnt += 1
        else:  # 2) 인접노드가 실외인데
            if not visited[i]:  # 방문한 적이 없으면 해당 실외노드부터 시작해서 다시 dfs 수행
                cnt = dfs(i, cnt)  # **주의 : 반환 값을 다시 cnt에 담아줘야함
    return cnt  # 호출된 함수가 종료될 때마다 계산된 실내노드 수를  반환


v = int(input())
location = [0]+list(map(int, list(input().rstrip())))
graph = [[] for _ in range(v+1)]

ans = 0
for _ in range(v-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    if location[a] == 1 and location[b] == 1:
        ans += 2

visited = [False]*(v+1)
for start in range(1, v+1):  # 시작노드 선정
    if not visited[start] and location[start] == 0:  # 현재 노드가 실외일 때 && 방문한적이 없을 때
        temp = dfs(start, 0)  # dfs 수행
        ans += temp*(temp-1)  # 실내 노드 수 구한 뒤 시작노드 선정 가지수(n-1)*도착노드선정 가지수n 하여 누적
print(ans)

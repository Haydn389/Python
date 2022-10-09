#https://velog.io/@letsbebrave/%EB%B0%B1%EC%A4%80-21606-%EC%95%84%EC%B9%A8-%EC%82%B0%EC%B1%85-4i69dxml
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input()) # 정점의 수
place = [0] + list(map(int, list(input().strip()))) # 1은 실내, 0은 실외
graph = [[] for _ in range(N+1)] # 노드
visited = [False] * (N+1) # 방문 기록

# 간선 정보 입력
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 실외와 인접한 실내의 개수 구하기
def dfs(v):
    visited[v] = True

    home_cnt = 0
    for i in graph[v]: # i의 인접노드 j
        if place[i] == 1: # 실내일 때
            home_cnt += 1
        else: # 실외일 때
            if not visited[i]: # 실외에 방문한 적 없을 때
                # visited[i] = True
                home_cnt += dfs(i)
    return home_cnt

cnt = 0

# 인접 경로
for v in range(1, N+1):
    if place[v] == 1: # 현재 노드가 실내일 때
        for j in graph[v]: # 인접노드
            if place[j] == 1: # 실내일 때
                cnt += 1
    else: # 현재 노드가 실외일 때
        if not visited[v]: # tmp로 방향이 switch된 것도 다 고려해주는 것! -> visited처리를 해줘야 중복 피할 수 있음
            # visited[v] = True
            tmp = dfs(v)
            cnt += tmp * (tmp-1) 

print(cnt)
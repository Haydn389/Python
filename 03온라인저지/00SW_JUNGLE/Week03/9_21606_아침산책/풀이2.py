#https://woonys.tistory.com/entry/%EC%A0%95%EA%B8%80%EC%82%AC%EA%B4%80%ED%95%99%EA%B5%90-22%EC%9D%BC%EC%B0%A8-TIL-%EC%95%84%EC%B9%A8-%EC%82%B0%EC%B1%85with-Python-%EC%9C%84%EC%83%81-%EC%A0%95%EB%A0%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
from sys import setrecursionlimit, stdin
setrecursionlimit(10**9)
"""문제 풀이 논리
1. 실외 점을 기준으로 인접해있는 실내 노드 개수를 count한다.
2. 실외 점을 중간에 놓고 실내 점 n개가 붙어있을 때 갈 수 있는 경로의 수는 n * 1(중간 실외 점 선택) * (n-1) = n*(n-1)에 해당.
3. 실외 노드끼리 연결되는 경우는 1) 실외끼리 인접 노드로 연결될 때 2) 중간에 실내 노드를 끼고 연결할 때. 이를 분리해서 생각.
"""
def dfs(v, cnt): # v: 정점 번호 & cnt: 실외와 연결된 실내 노드 개수 카운트
    
    visited[v] = True
    
    for i in graph[v]: # 노드 v와 연결된 인접 노드를 하나씩 불러온다.
        if location[i] == 1:  # 해당 노드의 위치가 실내이면
            cnt += 1 # 실내 개수 카운트에 +1을 해준다
        elif not visited[i]: # 방문하지 않고 해당 i 점의 위치가 실외이면
            cnt = dfs(i, cnt) # 해당 실외 점을 기준으로 dfs를 돈다!
    
    return cnt
ans = 0
n = int(stdin.readline()) # 정점 수 받기

location = [0]+list(map(int, stdin.readline().strip())) # location 정보 받아오기: 앞에 0 추가하는 이유는 노드의 인덱스 번호를 1부터 시작하기 위해

graph = [[] for _ in range(n+1)] # 1번 노드부터 n번 노드까지 다 받아와야 하니

for _ in range(n-1): # 셋째 줄부터 n+1번 줄까지 받기
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    if location[a] == 1 and location[b] == 1: # 둘다 실내이면
        ans +=2 # 서로 방문하는 케이스가 2가지이니 이걸 정답에 함께 바로 세는 걸로.
        
# sum = 0
visited = [False] * (n+1)
for i in range(1, n+1):
    if not visited[i] and location[i] == 0: # 실외인 애들을 기준으로
        x = dfs(i, 0) # 현재 cnt = 0
        ans += x*(x-1)  #실외인 노드를 기준으로 인접 노드 애들 개수 세는 게 총 n*(n-1)이니 실외 노드 걸릴 때마다 이걸 전부 세기

print(ans)
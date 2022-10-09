import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(v, group):
    visited[v] = group
    for i in graph[v]:
        if not visited[i]:  # 방문 안했으면 현재랑 다른그룹으로 설정해서 보내기
            temp = dfs(i, -group)
            if temp == False:
                return False
        elif visited[i] == visited[v]:  # 방문 한 노드인데 부모노드와 그룹이 동일함
            return False
    return True  # False를 한번도 만나지 않았다면 True 반환

n = int(input())
for _ in range(n):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False]*(v+1)
    for start in range(1, v+1):  # 연결요소가 1개가 아닐 수도 있기때문에 시작노드를 전부 다 돌려가면서
        if not visited[start]:  # 해당 노드가 not visited이면 다시 들어간다
            # 하지만 노드 돌려가면서 검사하는데 단 한번이라도 False가 나오면 break로 빠져나옴
            check = dfs(start, 1)
            if not check:
                break
    print("YES" if check else "NO")

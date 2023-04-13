#dfs로 방문하면서 색 칠하고 이미 칠해진 경우 현재 색과 비교하여 다른 지 검사
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

for _ in range(int(input().rstrip())):
    v,e=map(int,input().split())
    graph=[[] for _ in range(v+1)]
    
    for _ in range(e):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    def dfs(v,color):
        color*=-1
        visited[v]=color
        for i in graph[v]:
            if not visited[i]:#방문하지 않았다면 방문
                if dfs(i,color)==False:
                    return False
            elif visited[i]==visited[v]:#이미 방문했고 and 인접노드 색이 같다면
                return False
        return True

    visited=[0]*(v+1)
    for start in range(1,v+1):
        if not visited[start]:
            check=dfs(start,1)
            if not check:
                break
    print("YES" if check else "NO")
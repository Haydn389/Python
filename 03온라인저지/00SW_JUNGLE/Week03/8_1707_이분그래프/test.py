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
        visited[v]=color
        for i in graph[v]:
            if not visited[i]:#이전에 방문 안한 경우
                if dfs(i,-color)==True:#방문하면서 색 칠하기
                    return True
            elif visited[i]==visited[v]:#이전에 방문 했으나 & 부모의 색과 동일한 경우
                return True
        return False
    visited=[0]*(v+1)
    check=False
    for start in range(1,v+1):
        if visited[start]==0:
            if dfs(start,1)==True:
                check=True
                break
            
    if check==True:
        print("NO")
    else:
        print("YES")



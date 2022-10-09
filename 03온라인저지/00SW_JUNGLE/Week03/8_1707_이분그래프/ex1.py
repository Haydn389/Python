import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

def dfs(v,group):
    visited[v]=group
    for i in graph[v]:
        if not visited[i]:
            flag=dfs(i,-group)
            if not flag:
                return False
        elif visited[i]==visited[v]: #**오답 i 주의하기
            return False
    return True

n = int(input())
for _ in range(n):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited=[False]*(v+1)
    # flag=True
    for start in range(1,v+1):
        if not visited[start]:
            check=dfs(start,1)
            if check==False:
                break

    print("YES" if check else "NO")
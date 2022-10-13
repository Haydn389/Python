import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(v,group):
    visited[v]=group
    for i in graph[v]:
        if not visited[i]:
            check=dfs(i,-group)
            if not check:
                return False
        elif visited[i]==group:
            return False 
    return True

n=int(input())

for _ in range(n):
    v,e=map(int,input().split())
    graph=[[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited=[0]*(v+1)
    for start in range(1,v+1):
        if not visited[start]:
            flag=dfs(start,1)
            if not flag:
                break
    print("YES" if flag else "NO")
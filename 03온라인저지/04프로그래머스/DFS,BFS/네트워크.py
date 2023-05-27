
     
def solution(n, computers):
    graph=[[] for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            if i!=j and computers[i][j]:
                graph[i+1].append(j+1)
    # print(graph)
    visited=[False]*(n+1)

    def dfs(v):
        visited[v]=True
        # print(v)
        for i in graph[v]:
            if not visited[i]:
                dfs(i)
    cnt=0  
    for start in range(1,n+1):
        if not visited[start]:
            dfs(start)
            cnt+=1
    answer=cnt
    return answer
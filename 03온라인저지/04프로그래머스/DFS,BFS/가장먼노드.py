from collections import deque
def solution(n, edge):
    graph=[[] for _ in range(n+1)]
    for a,b in edge:
        graph[a].append(b) 
        graph[b].append(a) 
    visited=[-1]*(n+1)
    def bfs(start):
        q=deque([start])
        visited[start]=0
        while q:
            v=q.popleft()
            for i in graph[v]:
                if visited[i]==-1:
                    visited[i]=visited[v]+1
                    q.append(i)
                    
    print(visited)
    bfs(1)
    print(visited)
    
        
    answer = visited.count(max(visited))
    return answer
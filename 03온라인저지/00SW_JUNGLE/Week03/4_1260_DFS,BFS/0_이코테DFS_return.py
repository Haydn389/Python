def dfs(graph, v, visited):
    visited.append(v)
    print(v, end=" ")
    for i in graph[v]:
        if i not in visited:  # visited[i]==Falses
            dfs(graph, i, visited)
            # visited=dfs(graph, i, visited)
    # return visited

graph = [[], [2, 3, 8], [1, 7], [1, 4, 5],
         [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
visited=[]
dfs(graph,1,visited)
from collections import deque
def bfs(graph,v,visited):
    q=deque([v]) #큐에 담을 때 방문처리
    visited[v]=True
    while q:
        v=q.popleft() #팝하면서 출력
        print(v,end='')

        for i in graph[v]:
            if not visited[i]:
                q.append(i) #큐에 담을 때 방문처리
                visited[i]=True


# graph = [[], [2, 3, 8], [1, 7], [1, 4, 5],
#          [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5],
         [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

if __name__=="__main__":

    visited=[False]*(8+1) #간선의 갯수 +1

    bfs(graph,1,visited)
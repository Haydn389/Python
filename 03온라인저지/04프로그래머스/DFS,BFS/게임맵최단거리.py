from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y,maps,n,m):
    q=deque([(x,y)])
    maps[x][y]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and (maps[nx][ny]==1 or maps[nx][ny]==-1) :
                maps[nx][ny]=maps[x][y]+1
                q.append((nx,ny))
        # for map in maps:
        #     print(map)
        # print("-"*30)
        
def solution(maps):
    n=len(maps)
    m=len(maps[0])
    maps[n-1][m-1]=-1
        
    # for map in maps:
    #     print(map)
    # print("*"*30)
    bfs(0,0,maps,n,m)
    
    answer = maps[n-1][m-1]
    return answer
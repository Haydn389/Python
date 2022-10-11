# https://2hs-rti.tistory.com/entry/%EB%B0%B1%EC%A4%80-2665%EB%B2%88-%EB%AF%B8%EB%A1%9C%EB%A7%8C%EB%93%A4%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC

import sys
input=sys.stdin.readline
from collections import deque
dx=[-1,1,0,0]
dy=[0,0,1,-1]
n=int(input())
a=[list(map(int,list(input().rstrip()))) for _ in range(n)]

# print(a)
visited=[[-1]*n for _ in range(n)]


def bfs(x,y):
    q=deque()
    q.append((x,y))
    visited[x][y]=0
    while q:
        x,y=q.popleft()
        if x==n-1 and y==n-1:
            return visited[x][y]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==-1: #범위 내애 있고 아직 방문안했다면
                if a[nx][ny]==1: #!*** 흰방(1)이면 q 왼쪽에 담고 이전값으로 방문표시
                    q.appendleft((nx,ny))
                    visited[nx][ny]=visited[x][y]
                else:           #검은방(0) 이면 q에 담고 이전값+1로 방문표시
                    q.append((nx,ny))
                    visited[nx][ny]=visited[x][y]+1
        # print(visited)

print(bfs(0,0))
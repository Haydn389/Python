#https://door-of-tabris.tistory.com/entry/%EB%B0%B1%EC%A4%80-2665%EB%B2%88%EB%AF%B8%EB%A1%9C%EB%A7%8C%EB%93%A4%EA%B8%B0%ED%8C%8C%EC%9D%B4%EC%8D%AC
from heapq import heappush, heappop


n = int(input())
room = []
for _ in range(n):
    room.append(list(map(int, input().rstrip())))
visited = [[0] * n for _ in range(n)]


def dijkstra():
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    heap=[]
    heappush(heap,[0,0,0])
    visited[0][0]=True

    while heap:
        cnt,x,y=heappop(heap)
        if x==n-1 and y==n-1:
            print(cnt)
            return
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]

            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue

            if visited[nx][ny]==True:
                continue

            visited[nx][ny]=True
            if room[nx][ny]==0:
                heappush(heap,[cnt+1,nx,ny])
            elif room[nx][ny]==1:
                heappush(heap,[cnt,nx,ny])


dijkstra()
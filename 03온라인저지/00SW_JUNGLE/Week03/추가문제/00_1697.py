import sys
input=sys.stdin.readline
from collections import deque


start,end=map(int,input().split())
visited = [-1]*(100001)


def bfs(start):
    q=deque()
    q.append(start)
    visited[start]=0
    while q:
        now=q.popleft()
        if now==end:
            print(visited[end])
            break #!**********
        for next in [now-1,now+1,now*2]:
            if 0<=next<100001 and visited[next]==-1:
                visited[next]=visited[now]+1 #!*******
                q.append(next)
bfs(start)
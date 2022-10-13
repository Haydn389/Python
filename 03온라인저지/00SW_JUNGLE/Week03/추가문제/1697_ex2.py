import sys
input=sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

visited=[-1]*100001

def bfs(start):
    q=deque()
    q.append(start)
    visited[start]=0
    while q:
        v=q.popleft()
        #개수셀 때
        if v==m:
            print(visited[v])
            break
        for i in [v+1,v-1,v*2]:
            if 0<=i<100001 and visited[i]==-1:#!***범위주의
                visited[i]=visited[v]+1
                q.append(i)

bfs(n)
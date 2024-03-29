import sys
input=sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**12)

#노드 간선 수
v,e=map(int,input().split())
v=int(input())
e=int(input())
n, m = map(int, input().split())
m, n, h = map(int, input().split())

#공백없는 2차원 리스트
a = [list(map(int,list(input().rstrip()))) for _ in range(n)]
#공백있는 2차원 리스트
a = [list(map(int, input().split())) for _ in range(n)]
a = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

#방문처리
visited = [-1]*(v+1)
visited = [False]*(v+1)
visited = [[0] * n for _ in range(n)]

#그래프
graph=[[] for _ in range(v+1)]

#간선정보
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
#방향
dx=[0,1,0,-1]
dy=[1,0,-1,0]
#방향
dx=[-1,1,0,0]
dy=[0,0,-1,1]
x,y=0,0
for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i] 
    if 0<=nx<n and 0<=ny<m:
        pass
#q 선언
x=0
q = deque([x])

#다익스트라
import sys
input=sys.stdin.readline
from heapq import heappop,heappush
INF=int(1e9)
v=int(input())
e=int(input())
graph=[[] for _ in range(v+1)]
for _ in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((b,c)) #도착노드 , 비용 순으로 업데이트
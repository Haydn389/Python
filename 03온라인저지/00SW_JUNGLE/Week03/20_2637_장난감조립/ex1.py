from operator import ne
import sys
from collections import deque
input=sys.stdin.readline

v=int(input())
n=int(input())
graph=[[] for _ in range(v+1)]

needs = [[0] * (v+1) for _ in range(v+1)]
degree=[0]*(v+1)
for _ in range(n):
    a, b,c = map(int, input().split())#!** b->a로감
    graph[b].append((a,c))
    degree[a]+=1
q=deque()

for i in range(v+1):
    if degree[i]==0:
        q.append(i)

while q:
    now=q.popleft()

    for next,next_need in graph[now]:
        if needs[now].count(0)==v+1:
            needs[next][now]+=next_need
        else:
            for i in range(1,v+1):
                needs[next][i]+=needs[now][i]*next_need
        degree[next]-=1
        if degree[next]==0:
            q.append(next)

for x,y in enumerate(needs[v]):
    if y!=0:print(x,y)
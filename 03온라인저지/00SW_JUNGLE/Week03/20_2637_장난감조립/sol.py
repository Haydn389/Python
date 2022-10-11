#https://velog.io/@qweadzs/BOJ-2637-%EC%9E%A5%EB%82%9C%EA%B0%90-%EC%A1%B0%EB%A6%BDPython
import sys
from collections import deque
input=sys.stdin.readline

#노드 간선 수
v=int(input())
e=int(input())
graph=[[] for _ in range(v+1)]

# needs = [[0] * v for _ in range(v)] #!***index 다루기 편하게 하나씩 늘려주기!!
needs = [[0] * (v+1) for _ in range(v+1)]
degree=[0]*(v+1)
for _ in range(e):
    a, b,c = map(int, input().split())
    graph[b].append((a,c))  #!**주의 가리키는 방향이 a,b 반대임
    # degree[b]+=1             #! 방향이 b-->a 이므로 a로들어가는 indgree를 세주어야함
    degree[a]+=1

q=deque()
for i in range(1,v+1):
    if degree[i]==0:
        q.append(i)
res=[]

while q:
    now=q.popleft()
    # res.append(now)
    #next: 현재노드로 만들 수 있는 다음노드, 현재노드로 다음노드 만들 때 필요한 수
    for next,next_need in graph[now]:
        #기본 부품인경우
        if needs[now].count(0)==v+1:
            needs[next][now]+=next_need
        else:
            for i in range(1,v+1):
                needs[next][i]+=needs[now][i]*next_need
        # degree[i]-=1        #!*** 여기선 i가 아니라 next임
        degree[next]-=1       
        if degree[next]==0:
            q.append(next)

for x,y in enumerate(needs[v]):
    if y!=0:print(x,y)
# print(needs[v])
    # for i in graph[now]:
    #     degree[i]-=1
    #     if degree[i]==0:
    #         q.append(i)
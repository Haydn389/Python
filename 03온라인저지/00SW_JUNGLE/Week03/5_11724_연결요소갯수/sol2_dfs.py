import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
from collections import deque


def dfs(v):
    global res
    visited[v]=True
    # print(v,end=" ")
    # for i in sorted(graph[v]):
    flag=True
    for i in graph[v]:
        if not visited[i]:
            flag=False
            dfs(i)
    if flag:res+=1

if __name__ == "__main__":
    res=0
    v,e=map(int,input().split())
    graph = [[] for _ in range(v+1)] #메모리가 약간 더 적음
    start=0
    for _ in range(e):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    # for i in range(1,v+1):
    #     graph[i].sort()

    visited=[False]*(v+1)
    cnt=0       #시
    for i in range(1,v+1): #시작노드가 정해지지 않았기 때문에 반복문 돌리기
        if not visited[i]:
            cnt+=1
            dfs(i)
    # print()
    print(cnt)
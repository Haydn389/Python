#값 입력받기
#초기화- graph[], degree=0
#q 선언 및 degree 0인노드 push
#하나씩꺼내서 res리스트에담고, 인접노드의 degree -=1
#degree가 0이면 q.append() 반복

from collections import deque

v,e=map(int,input().split())
graph=[[] for _ in range(v+1)]
degree=[0]*(v+1)
for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
    degree[b]+=1
# print(degree)


res=[]
def topology_sort():
    q=deque()
    for i in range(1,v+1):
        if degree[i]==0:
            q.append(i)
    while q:
        now=q.popleft()
        res.append(now)
        for i in graph[now]:
            degree[i]-=1
            if degree[i]==0:
                q.append(i)


topology_sort()
print(res)
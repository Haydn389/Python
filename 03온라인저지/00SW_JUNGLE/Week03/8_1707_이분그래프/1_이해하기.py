#https://deep-learning-study.tistory.com/581
import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

def dfs(v,group):
    visited[v]=group
    # print(v,end="")
    for i in graph[v]:
        if not visited[i]:              #방문 안했으면 현재랑 다른그룹으로 설정해서 보내기
            temp=dfs(i,-group)
            if temp==False:
                return False
        elif visited[i]==visited[v]:    #방문 한 노드인데 부모노드와 그룹이 동일함
            return False
    return True                         #False를 한번도 만나지 않았다면 True 반환
# n=int(input())
# for _ in range(n):

v,e=map(int,input().split())
graph=[[] for _ in range(v+1)]
for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

group=[]
visited=[False]*(v+1)
for start in range(1,v+1):
    if not visited[start]:
        check=dfs(start,1)
        if not check:
            break
print("YES" if check else "NO")

#input
# 5 6
# 1 2
# 1 4
# 2 3
# 2 5
# 3 4
# 4 5
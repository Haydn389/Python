# 특정원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드 개수와 간선(union연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0]*(v+1)  # 부모테이블 초기화

#모든간선을 담을 리스트와 최종비용을 담을 변수
edges=[]
result=0

# 부모테이블상에서 부모를 자기자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

#모든 간선에 대한 정보 입력받기
for _ in range(e):
    a,b=map(int,input().split())
    edges.append((a,b))

# edges.sort()

for edge in edges:
    a,b=edge

    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        # result+=cost
print(parent)
print(result)
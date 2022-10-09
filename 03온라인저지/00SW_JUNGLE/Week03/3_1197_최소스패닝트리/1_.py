import sys
input = sys.stdin.readline

#특정원소가 속한 집합 찾기
def find(x):
    global p
    if p[x]!=x:
        p[x]=find(p[x])
    return p[x]

#두 원소가 속한 집합을 합치기
def union(a,b):
    global p
    a=find(a)
    b=find(b)
    if a<b:
        p[b]=a
    else:
        p[a]=b

if __name__ == '__main__':
    #노드개수와 간선 개수 입력받기
    v,e=map(int,input().split())

    edges=[]
    res=0

    #부모테이블에서 부모를 자기자신으로 초기화
    p=[0]*(v+1)
    for i in range(1,v+1):p[i]=i
    # p=[*range(v+1)]

    #모든 간선에 대한 정보 입력받기
    for _ in range(e):
        a,b,cost=map(int,input().split())
        edges.append((cost,a,b))

    edges.sort()

    for edge in edges:
        cost,a,b=edge

        if find(a)!=find(b):
            union(a,b)
            res+=cost
    print(res)
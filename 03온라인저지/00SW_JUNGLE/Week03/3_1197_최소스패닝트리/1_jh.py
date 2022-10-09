import sys
input = sys.stdin.readline

def find_root(node : int) -> int:
    global parent

    if node != parent[node]:
        parent[node] = find_root(parent[node])
    return parent[node]


def union(node1 : int, node2 : int) -> int:
    '''경로 압축'''
    global parent

    if parent1 < parent2:
        parent[parent2] = parent1
    else:
        parent[parent1] = parent2


if __name__ == '__main__':
    V, E = map(int, input().split())

    parent = [*range(V + 1)] # 0도 있어야됨. idx가 겹치지 않기 위해.

    Elist = []
    for _ in range(E):
        '''A,B : node, C : weight '''
        A, B, C = map(int, input().split())
        Elist.append([A, B, C])
    Elist.sort(key=lambda x:x[2]) # Kruskal을 사용할 것이기 때문에 가중치 기준 정렬이 필요

    sum = 0
    for node1, node2, weight in Elist:
        parent1 = find_root(node1)
        parent2 = find_root(node2)
        if parent1 != parent2:  # 만약 부모가 같지 않으면, 즉 사이클이 아니면.
            union(node1, node2)
            sum += weight
    print(sum)
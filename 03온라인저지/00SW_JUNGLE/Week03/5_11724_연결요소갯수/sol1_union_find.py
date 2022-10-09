import sys
input = sys.stdin.readline

def find(x):
    global p
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(a, b):
    global p
    a = find(a)
    b = find(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b

if __name__ == "__main__":
    v, e = map(int, input().split())
    p = [*range(1+v)]
    edges = []

    for _ in range(e):
        a, b = map(int, input().split())
        edges.append((a, b))
    res = 0

    for edge in edges:
        a, b = edge
        if find(a) != find(b):
            union(a, b)

# print(p)
ans = []
for i in p:
    ans.append(find(i))

print(len((set(ans[1:]))))

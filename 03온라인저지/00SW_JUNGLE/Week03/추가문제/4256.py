import sys
input = sys.stdin.readline

# n=int(input())

# for _ in range(n):
v = int(input())
pre_order = list(map(int, input().split()))
in_order = list(map(int, input().split()))
print(pre_order)
print(in_order)
res = []

def post(root, start, end):
    rootnode = pre_order[root]
    for i in range(start, end+1):
        if in_order[i] == rootnode:
            post(root+1, start+1, i)
            post(root+i+1, i+1, end)
            res.append(rootnode)


post(0, 0, v-1)
print(res)
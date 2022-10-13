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

def post(s,e):
    if s>e:
        return
    mid=-1
    for i in range(s+1,e):
        if pre_order[s]==in_order[i]:
            mid=i
            break
    post(s,mid-1)
    post(mid+1,e-1)
    print(pre_order[s])


post(0, v-1)
print(res)
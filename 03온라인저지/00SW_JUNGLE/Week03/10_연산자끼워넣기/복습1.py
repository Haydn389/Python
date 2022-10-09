import sys

input = sys.stdin.readline


n = int(input())
a = list(map(int, input().split()))
oper = list(map(int, input().split()))
res=0
max_res=-1e9
min_res=1e9
def cal(i, res):
    global max_res,min_res
    # 기저조건
    if i == n:
        max_res=max(max_res, res)
        min_res=min(min_res, res)

    else:
        if oper[0] > 0:
            oper[0] -= 1
            cal(i+1, res+a[i])
            oper[0] += 1
        if oper[1] > 0:
            oper[1] -= 1
            cal(i+1, res-a[i])
            oper[1] += 1
        if oper[2] > 0:
            oper[2] -= 1
            cal(i+1, res*a[i])
            oper[2] += 1
        if oper[3] > 0:
            oper[3] -= 1
            cal(i+1, int(res/a[i])) #주의 a//b int(a/b) a가음수일때 차이남
            oper[3] += 1

cal(1, a[0])
print(max_res)
print(min_res)

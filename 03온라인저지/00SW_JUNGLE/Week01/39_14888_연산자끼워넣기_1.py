from itertools import permutations
n = int(input())
o = ['+', '-', '*', '/']
num = list(map(int, input().split()))
op = list(map(int, input().split()))  # + - * /
oper = []
for i in range(4):
    for j in range(op[i]):
        oper.append(o[i])

oper = set(permutations(oper, n-1))  # 중복제거
# print(oper)
answer = []
ans_max = -1e9
ans_min = 1e9
print(oper)
for o in oper:
    tot = num[0]
    for i in range(n-1):
        if o[i] == "+":
            tot += num[i+1]
        elif o[i] == "-":
            tot -= num[i+1]
        elif o[i] == "*":
            tot *= num[i+1]
        else:
            tot = int(tot/num[i+1])
    if tot > ans_max:
        ans_max = tot
    if tot < ans_min:
        ans_min = tot

print(ans_max)
print(ans_min)

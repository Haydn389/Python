import sys
n = int(sys.stdin.readline())

for _ in range(n):
    stack = []
    cmd = sys.stdin.readline().rstrip()
    # flag=True
    for p in cmd:
        if not stack:           # 비어있으면 (비어있으면 stack 이 Fasle 인데 not을 붙여서)
            stack.append(p)     # 그리고 ")"가 들어오면 break 즉,(비어있는 상태에서 ")"가 들어오면)
            if p == ")":
                break
        else:                   # 비어있지 않으면
            if p == "(":        # 그리고 "("가 들어오면 append
                stack.append(p) # 또는 ")"가 들어오면 pop
            else:
                stack.pop()
    if stack:                   # 비어있지 않으면 (즉 남아있는 괄호가 있다면)
        print("NO")
    else:
        print("YES")


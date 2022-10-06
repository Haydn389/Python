import sys
n = int(sys.stdin.readline())


for i in range(n):
    stack=[]
    cmd=sys.stdin.readline().rstrip()
    for p in cmd:
        if not stack:
            stack.append(p)
            if p==")":
                break
        else:
            if p=="(":
                stack.append(p)
            else:
                stack.pop()
    if stack:
        print("NO")
    else:
        print("YES")
import sys
input=sys.stdin.readline

n=int(input())

for _ in range(n):
    cmd=input().rstrip()

    stack=[]
    for p in cmd:
        if not stack:
            stack.append(p)
            if p==")":
                break
        else:
            if p =="(":
                stack.append(p)
            else:
                stack.pop()

    if stack:
        print("NO")
    else:
        print("YES")    
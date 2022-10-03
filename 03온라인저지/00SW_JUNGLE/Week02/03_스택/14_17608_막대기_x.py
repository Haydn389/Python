#이전에 들어온 값보다 현재 값이 작으면 push(1) 아니면 pop()

import sys
n = int(sys.stdin.readline())

stack=[]
stack.append(int(sys.stdin.readline()))

for _ in range(n-1):
    top=stack[-1]
    cmd=int(sys.stdin.readline())
    if top<cmd:
        while top<=cmd:
            stack.pop()
            try:
                top=stack[-1]
            except IndexError:
                top=1e9
        stack.append(cmd)
        # print(stack)
    else:
        stack.append(cmd)
        # print(stack)

print(len(stack))
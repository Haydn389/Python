import sys
n = int(sys.stdin.readline())

stack=[]
for i in range(n):
    cmd=int(sys.stdin.readline())

    if cmd!=0:
        stack.append(cmd)
        # print(stack)
    else:
        stack.pop()
        # print(stack)


print(sum(stack))
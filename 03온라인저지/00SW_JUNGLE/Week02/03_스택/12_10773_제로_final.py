import sys
input = sys.stdin.readline
n = int(input())
# a= list(int(input()) for _ in range(n))

stack=[]
for i in range(n):
    cmd=int(input())
    if cmd!=0:
        stack.append(cmd)
    else:
        stack.pop()

print(sum(stack))
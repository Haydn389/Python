import sys
input = sys.stdin.readline
n, k = map(int, input().split())
s = input().rstrip()

cnt = k
stack = []
for num in s:
    while len(stack) != 0 and cnt > 0 and stack[-1] < num:
        stack.pop()
        cnt -= 1
    stack.append(num)

print("".join(stack)[:n-k]) #

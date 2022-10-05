from collections import deque
import sys
q=deque()

n=int(sys.stdin.readline())
# n=6
for i in range(n,0,-1):
    q.append(i)
# print(q)
while len(q)>1:
    q.pop()
    q.appendleft(q.pop())

print(q.popleft())
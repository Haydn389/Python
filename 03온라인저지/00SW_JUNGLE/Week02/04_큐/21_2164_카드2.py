from collections import deque
import sys
q=deque()

n=int(sys.stdin.readline())
# n=6
for i in range(1,n+1):
    q.append(i)

while len(q)>1:
    q.popleft()
    q.append(q.popleft())

print(q.pop())
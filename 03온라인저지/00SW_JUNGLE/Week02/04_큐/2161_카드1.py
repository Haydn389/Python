from collections import deque
import sys
q=deque()
n=int(sys.stdin.readline())
for i in range(1,n+1):
    q.append(i)

while len(q)>1:
    print(q.popleft(),end=" ")
    q.append(q.popleft())
    # print(q)
print(q[0])
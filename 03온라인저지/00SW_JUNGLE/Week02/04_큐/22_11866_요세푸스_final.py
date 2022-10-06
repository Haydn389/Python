from collections import deque
import sys

n,k=map(int,sys.stdin.readline().split())

q=deque()

for i in range(1,n+1):q.append(i)
ans=[]
while len(q)>0:
    for _ in range(k-1):
        q.append(q.popleft())
    ans.append(str(q.popleft()))

# print(*ans)
print("<"+', '.join(ans)+">")
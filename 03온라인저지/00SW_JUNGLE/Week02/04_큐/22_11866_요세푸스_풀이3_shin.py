from collections import deque
from random import randrange
import sys

n,m=map(int,sys.stdin.readline().split())
n,m=7,3
q=deque()
ans=[]
for i in range(n):
    q.append(i+1)
# print(q)


while len(q) > 1:
    for i in range(1, m):
        q.append(q.popleft())
    ans.append(str(q.popleft())) # k-th number is deleted
# ans.append(q.popleft()) # len(q) == 1
# print(ans)

while len(q)>1:
    for i in range(1,m):
        q.append(q.popleft())
    ans.append(str(q.popleft())) 
print("<",', '.join(ans),">", sep="")

import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
dist=[0] *100001

q=deque()
q.append(n)
while q:
    now=q.popleft()
    if now==k:
        print(dist[now])
        break
    for new in [now-1,now+1,now*2]:
        if 0<=new<100001 and dist[new]==0:
            dist[new]=dist[now]+1
            q.append(new)

# 5 17

#정답 : 4
import sys
from collections import deque
input=sys.stdin.readline

n,k=map(int,input().split())
time=[0]*100001
q=deque([n])

while q:
    now=q.popleft()
    if now==k:
        print(time[now])
        break
    for new in [now-1,now+1,now*2]:
        if 0<=new<=100001 and time[new]==0:
            time[new]=time[now]+1
            q.append(new)

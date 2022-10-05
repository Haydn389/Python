from collections import deque
import sys

n,m=map(int,sys.stdin.readline().split())
# n,m=7,3
q=deque()
ans=[]
for i in range(n):
    q.append(i+1)
# print(q)
# idx=0
# while len(q)>0:
cnt=1
while len(q)>0:
    temp=q.popleft()
    if cnt%m==0:
        ans.append(temp)
        cnt=0
    else:
        q.append(temp)
    cnt+=1

print(ans)
print("<",', '.join(ans),">", sep="")

# print("<",end="")
# for a in ans[:n-1]:
#     print(a,end=", ")
# print(ans[n-1],end="")
# print(">",end="")
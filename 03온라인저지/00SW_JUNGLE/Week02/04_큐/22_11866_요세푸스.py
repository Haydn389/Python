from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
# n,m=7,3
q = deque()
for i in range(n):
    q.append(i+1)

ans = []
cnt = 1
while len(q) > 0:
    temp = q.popleft()
    if cnt % m == 0:
        ans.append(str(temp)) #애초에 받을 때 str()로 받자
        cnt = 0
    else:
        q.append(temp)
    cnt += 1

print(ans)
# ans=list(map(str,ans))
print("<", ', '.join(ans), ">", sep="")

# print("<",end="")
# for a in ans[:n-1]:
#     print(a,end=", ")
# print(ans[n-1],end="")
# print(">",end="")

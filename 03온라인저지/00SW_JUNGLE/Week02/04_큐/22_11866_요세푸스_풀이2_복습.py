from collections import deque

n,k=map(int,input().split())
nums=[i+1 for i in range(n)]
q=deque(nums)
ans=[]
print(q)
for i in range(n):
	q.rotate(-k)
	print(q)
	ans.append(str(q[-1]))
	# q.pop()

print("<",', '.join(ans),">",sep="")
from collections import deque

n,k=map(int,input().split())
nums=[i+1 for i in range(n)] 
q=deque(nums)
arr=[]

for i in range(len(nums)):
	q.rotate(-k)
	arr.append(str(q[-1]))
	q.pop()

print("<",', '.join(arr),">", sep="")
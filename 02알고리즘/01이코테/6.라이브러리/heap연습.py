from heapq import heappop,heappush,heapify,heappushpop,nsmallest,nlargest

arr=[-1,0,-8,1,5,6,-7,-4,-3,10]

h=[]
res=[]
for v in arr:
    heappush(h,-v)

for i in range(len(h)):
    res.append(-heappop(h))
print(res)
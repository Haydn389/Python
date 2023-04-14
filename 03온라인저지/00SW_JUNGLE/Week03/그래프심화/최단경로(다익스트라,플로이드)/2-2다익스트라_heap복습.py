from heapq import heappush,heappop,heappushpop,heapify,nsmallest,nlargest
import copy


arr=[1,2,3,4,5,6,7]
n=len(arr)
print(nsmallest(3,arr))
print(nlargest(3,arr))

print("min-heap")
min_heap=arr[:]
heapify(min_heap)
for _ in range(n):
    print(heappop(min_heap), end=" ")

print("\nmax-heap")
max_heap=[]
for v in arr:
    heappush(max_heap,-v)

for _ in range(n):
    print(-heappop(max_heap), end=" ")
# heappush(heap,10)
# heappop(heap)
# print(heappushpop(heap,20))



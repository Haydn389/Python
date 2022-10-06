from heapq import heapify,heappop,heappush
import heapq
heap=[]
heapq.heappush(heap,4)
heapq.heappush(heap,1)
heapq.heappush(heap,7)
heapq.heappush(heap,3)
print(heap) # [1,3,7,4]

print(heapq.heappop(heap)) #1
print(heap) # [3,4,7]

print(heapq.heappop(heap)) #3
print(heap) # [4,7]

print(heap[0])

#기존 리스트를 힙으로 변환
h1=[4,1,7,3,8,5]
heapq.heapify(h1)
print(h1) #[1,3,5,4,8,7]
print("*"*50)
nums = [4, 1, 7, 3, 8, 5]

heap2 = nums[:]
heap2 = [*nums]
heapq.heapify(heap2)

print(nums) #[4,1,7,3,8,5]
print(heap2) #[1,3,5,4,8,7]
print("*"*50)
#n번째 최솟값/최댓값

print(heapq.nsmallest(3, [4, 1, 7, 3, 8, 5])) #[1,3,4]
print(heapq.nsmallest(3, [4, 1, 7, 3, 8, 5])[-1]) #4

print("*"*50)
def nth_smallest(nums,n):
    heapq.heapify(nums)
    nth_min=0
    for _ in range(n):
        nth_min=heapq.heappop(nums)
    return nth_min
print(nth_smallest([4,1,7,3,8,5],3)) #4

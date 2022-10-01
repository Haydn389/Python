import heapq
import sys
def heapsort(array):
    h=[]
    result=[]
    for i in array:
        heapq.heappush(h,i)
    for _ in range(len(h)):
        result.append(heapq.heappop(h))

    return result

data=list(map(int,sys.stdin.readline().split()))


result = heapsort(data)
print(result)
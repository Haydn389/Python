import heapq

def heapsort(array):
    h=[]
    result=[]

    for i in array:
        heapq.heappush(h,i)
    for j in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result=heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

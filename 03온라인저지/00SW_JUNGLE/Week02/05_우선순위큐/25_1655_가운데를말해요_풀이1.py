#https://inspirit941.tistory.com/200
import heapq
import sys

left,right=[],[]


n=int(sys.stdin.readline())

for _ in range(n):
    num=int(sys.stdin.readline())
    if len(left) == len(right):
        #max_heapq.
        heapq.heappush(left,(-num,num))

    else: #min_heapq.
        heapq.heappush(right,(num,num))
    
    #오른쪽 값에 원소가 있으면서,
    #왼쪽값이 오른쪽값보다 큰경우.. left 원소보다 right원소보다 더 커야하는 조건에 위배
    if right and left[0][1] > right[0][1]: #left[0], right[0] 는 각각의 힙의 최상단 노드(root node)를 의미함
        left_val=heapq.heappop(left)[1]
        right_val=heapq.heappop(right)[1]
        heapq.heappush(right, (left_val,left_val))
        heapq.heappush(left, (-right_val,right_val))

    print(left[0][1])
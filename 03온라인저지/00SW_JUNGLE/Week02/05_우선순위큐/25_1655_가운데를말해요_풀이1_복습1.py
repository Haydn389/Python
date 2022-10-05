import sys
import heapq
input=sys.stdin.readline
n=int(input())
left=[]
right=[]
for _ in range(n):
    num=int(input())
    if len(left)==len(right):
        heapq.heappush(left,(-num,num))
    else:
        heapq.heappush(right,(num,num))

    #right에 값이 있고 and left의 루트노드값이 right의 루트노드값보다 클때 서로교환
    if right and left[0][1] > right[0][1]:
        left_val=heapq.heappop(left)[1]
        right_val=heapq.heappop(right)[1]
        heapq.heappush(left,(-right_val,right_val))
        heapq.heappush(right,(left_val,left_val))

    print(left[0][1])
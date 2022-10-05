import sys
import heapq
import math
input=sys.stdin.readline
n=int(input())
h=[]

for _ in range(n):
    heapq.heappush(h,int(input()))
    half=math.ceil(len(h)/2)
    # print("half",half)
    # print(f"{half}번째 값",heapq.nsmallest(half,h))
    print(heapq.nsmallest(half,h)[-1])

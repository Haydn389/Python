import sys
import heapq
input=sys.stdin.readline
n=int(input())
h=[]

def nth_smallest(half):
    global h
    nth_min=None
    temp=[]
    for _ in range(half):
        nth_min=heapq.heappop(h)
        temp.append(nth_min)
    for t in temp:
        heapq.heappush(h,t)
    return nth_min

for _ in range(n):
    heapq.heappush(h,int(input()))
    if len(h)%2==0:
        half=len(h)//2
    else: half=len(h)//2+1
    print(nth_smallest(half))


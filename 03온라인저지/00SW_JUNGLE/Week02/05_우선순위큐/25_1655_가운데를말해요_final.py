from heapq import heapify,heappop,heappush
import sys

input=sys.stdin.readline
n=int(input())
h_max=[]
h_min=[]
for i in range(n):
    num=int(input())
    if i%2==0:
        heappush(h_max,(-num,num))
    else:
        heappush(h_min,(num,num))
    
    if h_min and h_max[0][1]>h_min[0][1]:
        l_val=heappop(h_max)[1]
        r_val=heappop(h_min)[1]
        heappush(h_max,(-r_val,r_val))
        heappush(h_min,(l_val,l_val))
    print(h_max[0][1])
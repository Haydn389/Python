import heapq

n=int(input())

h=list(int(input()) for _ in range(n))
heapq.heapify(h)

res=0

while len(h)>1:
    a=heapq.heappop(h)
    b=heapq.heappop(h)
    res+=(a+b)
    heapq.heappush(a+b)
print(res)
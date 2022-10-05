#https://derekahndev.github.io/problem%20solving/boj-2014/
#https://deok2kim.tistory.com/232
#https://seokjin2.tistory.com/31 마지막 조건
# https://loosie.tistory.com/719 마지막 조건
import heapq

k, n = map(int, input().split())
data = list(map(int, input().split()))
heap = []

for d in data:
    heapq.heappush(heap, d)

for _ in range(n):
    num = heapq.heappop(heap)
    for i in range(k):
        temp = num * data[i]
        heapq.heappush(heap, temp)

        if num % data[i] == 0:
            break

print(num)

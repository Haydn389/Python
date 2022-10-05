import sys
import heapq
input = sys.stdin.readline

k, n = map(int, input().split())
a = list(map(int, input().split()))
k,n=4,19
a=[2,3,5,7]
h = [*a]
heapq.heapify(h)
for _ in range(n):
    num = heapq.heappop(h)
    for i in range(k):
        temp = num*a[i]
        heapq.heappush(h, temp)
        if num % a[i] == 0:
            break
print(num)

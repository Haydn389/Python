# https://velog.io/@piopiop/%EB%B0%B1%EC%A4%80-13334-%EC%B2%A0%EB%A1%9C%ED%8C%8C%EC%9D%B4%EC%8D%AC
# https://yongjoonseo.dev/problem%20solving/python/PS-baekjoon037/

import sys
input = sys.stdin.readline
from heapq import heappush, heappop

def solution(n):
    lst = [sorted(list(map(int, input().split()))) for i in range(n)]
    lst.sort(key=lambda x: x[1])
    d = int(input())
    result = -1
    heap = []
    for s, e in lst:
        lim = e - d
        if s >= lim:
            heappush(heap, s)
        while heap and heap[0] < lim:
            heappop(heap)
        result = max(result, len(heap))
    print(result)

if __name__ == '__main__':
    solution(int(input()))
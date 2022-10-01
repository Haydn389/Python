from itertools import combinations
import sys
n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
cnt = 0

for i in range(1, n+1): #nC1, nC2, ... nCn까지 모든 경우의 수 산출
    for com in combinations(a, i):  
        if sum(com) == m:   #각 case에서의 부분합이 m과 같은지 검토
            cnt += 1
print(cnt)

import sys
from itertools import permutations

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))

per_arr=list(permutations(arr))
# per_arr = permutations(arr) 이렇게도 가능! 다만 리스트가 아님
ans = 0
for A in per_arr:
    s = 0
    # print(A)
    for i in range(n-1):
        s += abs(A[i]-A[i+1])
    if s > ans:
        ans = s

print(ans)

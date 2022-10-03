# 두번째 방법
import sys
input = sys.stdin.readline

n = int(input())
sticks = [int(input()) for _ in range(n)]
max_height = sticks[-1]
cnt = 1

for i in range(n):
    temp = sticks.pop()
    if max_height < temp:
        cnt += 1
        max_height = temp
print(cnt)

#이전에 들어온 값보다 현재 값이 작으면 push(1) 아니면 pop()
import sys
input = sys.stdin.readline
 
n = int(input())
sticks = [int(input()) for _ in range(n)]
# n=6
# sticks=[6,9,7,6,4,6]

max_height = sticks[-1]
cnt = 1
 
for i in range(n,0,-1):
    if max_height < sticks[i-1]:
        cnt += 1
        max_height = sticks[i-1]
print(cnt)
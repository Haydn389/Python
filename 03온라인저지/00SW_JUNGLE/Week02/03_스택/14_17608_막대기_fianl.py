import sys
input=sys.stdin.readline

n=int(input())

a=[int(input().rstrip()) for _ in range(n)]

cnt=1
max_a=a.pop()
for _ in range(n-1):
    temp=a.pop()
    if max_a<temp:
        cnt+=1
        max_a=temp
print(cnt)
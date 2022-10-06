import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))

stack=[]

ans=[0]*n
for i in range(n):
    while stack and stack[-1][1]<=a[i]:
        stack.pop()
    if stack:
        ans=stack[-1][0]
    stack.append([i+1,a[i]])
print(*ans)
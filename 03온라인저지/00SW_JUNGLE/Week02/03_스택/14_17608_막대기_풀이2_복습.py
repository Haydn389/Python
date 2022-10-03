import sys
input=sys.stdin.readline
n=int(input())
stack=[int(input()) for _ in range(n)]

cnt=1
top=stack.pop()

for i in range(n-1):
    temp=stack.pop()
    if top<temp:
        cnt+=1
        top=temp
print(cnt)

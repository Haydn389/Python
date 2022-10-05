import sys
input = sys.stdin.readline
# n=7
# a=[2,1,4,5,1,3,3]
# n=10
# a=[5,10,3,7,12,5,7,2,10,7]
# n=5
# a=[1,2,3,4,5]

while True:
    n,*a=list(map(int, input().split()))
    if n==0:break
    stack=[]
    left=[-1]*n
    for i in range(n):
        while stack and stack[-1][-1]>=a[i]:
            stack.pop()
        if stack:
            left[i]=stack[-1][0]
        stack.append([i,a[i]])
    # print(left)
    stack=[]
    right=[n]*n
    for i in range(n-1,-1,-1):
        while stack and stack[-1][-1]>=a[i]:
            stack.pop()
        if stack:
            right[i]=stack[-1][0]
        stack.append([i,a[i]])
    # print(left)

    area=[(right[i]-left[i]-1)*a[i] for i in range(n)]
    print(max(area))
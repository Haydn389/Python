import sys
input = sys.stdin.readline
# n=7
# a=[2,1,4,5,1,3,3]
# n=10
# a=[5,10,3,7,12,5,7,2,10,7]
# n=5
# a=[1,2,3,4,5]

while True:
    a = list(map(int, sys.stdin.readline().split()))    
    if a[0] == 0:
        break
    n = a[0]
    a = a[1:]
    #--------------------------------------------#
    area = [None]*n
    stack = []
    left = [-1]*n
    for i in range(n):  # 0~n-1
        while stack and stack[-1][1] >= a[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1][0]
        stack.append([i, a[i]])
    stack = []
    right = [n]*n  # 오른쪽 넘어선 인덱스 초기화 ex) 10
    for i in range(n-1, -1, -1):  # n-1 ~ 0 
        while stack and stack[-1][1] >= a[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1][0]
        stack.append([i, a[i]])

    area = [(right[i]-left[i]-1)*a[i] for i in range(n)]
    print(max(area))

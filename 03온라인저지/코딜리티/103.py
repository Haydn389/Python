import sys
input=sys.stdin.readline

def solution(A):
    A.sort()
    a=[]
    stack=[]
    temp=0
    for i in A:
        if temp!=i:
            a.append(i)
            temp=i
        else:
            stack.append(i)
    print(a)
    print(stack)

    while stack:
        temp=stack.pop()
        if a[-1]!=temp:
            a.append(temp)
    # print(a)
    return len(a)

A=list(map(int,input().split()))
print(solution(A))
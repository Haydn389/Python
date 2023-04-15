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
            if not stack or stack[-1]!=i:#개선
                stack.append(i)
    print(a)
    print(stack)
    #개선
    ans=len(a)+len(stack)
    if stack and a[-1]==stack[-1]:
        return ans-1
    else:
        return ans
    #개선
    
    while stack:
        temp=stack.pop()
        if a[-1]!=temp:
            a.append(temp)
    # print(a)
    return len(a)

A=list(map(int,input().split()))
print(solution(A))
import sys
input=sys.stdin.readline

def solution(H):
    cnt=0
    stack=[]
    for i in H:
        while stack and stack[-1]>i:#스택값이 있고, 새 값이 기존값보다 작은동안
            stack.pop()
        if not stack or stack[-1]<i:#스택값이 없거나, 새 값이 기존값보다 클때
            cnt+=1
            stack.append(i)
        print(stack,cnt)

    return cnt

A=list(map(int,input().split()))
print(solution(A))
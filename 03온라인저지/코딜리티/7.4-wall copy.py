import sys
input=sys.stdin.readline

def solution(H):
    stack=[]
    cnt=0
    for i in H:
        while(stack and stack[-1]>i):
            stack.pop()
        if not stack or stack[-1]<i:
            cnt+=1
            stack.append(i)   
    #스택이 있고 새 값이 기존값보다 작은동안
    #스택이 없거나 새 값이 기존값보다 클때
    return cnt
A=list(map(int,input().split()))
print(solution(A))
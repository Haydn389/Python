import sys
input=sys.stdin.readline

def solution(A,B):
    fish=[]
    for i,v in enumerate(A):
        fish.append([v,B[i]])
    stack=[]
    for p in fish:
        if p[1] ==0: #왼쪽
            if stack and stack[-1][1]==1:#마지막 원소가 오른쪽으로 가는 물고기
                    if stack[-1][0] <= p[0]:
                        stack.pop()
                        stack.append(p)
            else: 
                stack.append(p)
        else:#오른쪽
            stack.append(p)
    pre=len(stack)
    post=-1
    while pre!=post:
        stack2=[]
        for p in stack:
            if p[1] ==0: #왼쪽
                if stack2 and stack2[-1][1]==1:#마지막 원소가 오른쪽으로 가는 물고기
                        if stack2[-1][0] <= p[0]:
                            stack2.pop()
                            stack2.append(p)
                else: 
                    stack2.append(p)
            else:#오른쪽
                stack2.append(p)
        pre=len(stack)
        post=len(stack2)
        stack=stack2
        

    return len(stack)

A=list(map(int,input().split()))
B=list(map(int,input().split()))
print(solution(A,B))
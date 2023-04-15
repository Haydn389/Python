import sys
input=sys.stdin.readline

def solution(S):
    stack=[]
    left=['{','[','(']
    right=['}',']',')']
    for p in S:
        if not stack:   #비어있으면
            stack.append(p)
            if p in right:
                break
        else:   #안비어있으면
            if p in right:  #
                if left.index(stack[-1])==right.index(p):
                    stack.pop()
                else:
                    break
            else:
                stack.append(p)
    if stack:
        return 0
    else: return 1

S=input().rstrip()
print(solution(S))
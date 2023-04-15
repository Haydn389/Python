import sys
input=sys.stdin.readline

def solution(A,B):
    fish=[]
    for i,v in enumerate(A):
        fish.append([v,B[i]])
    stack=[]
    for p in fish:
        if p[1] ==0: #왼쪽
            if stack and stack[-1][1]==1:
                while(True): #마지막 원소가 오른쪽으로 가는 물고기
                    if stack[-1][0] < p[0]:
                        stack.pop()
                        if len(stack)==0 or stack[-1][1]==0:
                            stack.append(p)
                            break
                    else:
                        break
            else: 
                stack.append(p)
        else:#오른쪽
            stack.append(p)
    return len(stack)
A=list(map(int,input().split()))
B=list(map(int,input().split()))
print(solution(A,B))
import sys
input=sys.stdin.readline

def solution(A,B):
    arr=[]
    for i,v in enumerate(A):
        arr.append([v,B[i]])

    stack=[]
    stack.append(arr[0])
    # print(arr)
    # print(stack)
    for i in range(1,len(arr)):
        while(True):
            if arr[i][1]==0 and stack[-1][1]==1:#충돌조건
                #기존 물고기가 더 쎔
                if arr[i][0] < stack[-1][0]:
                    break
                else:
                    stack.pop()
                    if len(stack)==0:
                        stack.append(arr[i])
                        break
                # 새로운 물고기가 더 쎔                
            else:
                stack.append(arr[i])
                break

    return len(stack)

A=list(map(int,input().split()))
B=list(map(int,input().split()))
print(solution(A,B))
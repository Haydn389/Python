import sys
input=sys.stdin.readline

def solution(A):
    if len(A)==1:
        return A[0]
    max_end=0 # 
    max_slice=0 #현재까지 최댓값
    for a in A:
        max_end=max(0,max_end+a)
        max_slice=max(max_slice,max_end)
    return max(0,max_slice)

A=list(map(int,input().split()))
print(solution(A))
import sys
input=sys.stdin.readline

def solution(A):
    if len(A)<=1:
        return 0
    min_v=A[0] #이전단계까지 가장 작은값 저장
    max_v=0 #이전단꼐까지 이익의 최댓값 저장
    for a in A[1:]:
        max_v=max(max_v,a-min_v)
        min_v=min(min_v,a)

    return max_v

A=list(map(int,input().split()))
print(solution(A))
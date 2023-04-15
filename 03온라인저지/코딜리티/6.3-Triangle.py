import sys
input=sys.stdin.readline

def solution(A):
    A.sort()
    for i in range(len(A)-2):
        if A[i]+A[i+1] > A[i+2]:
            if A[i]+A[i+2] > A[i+1]:
                if A[i+2]+A[i+1] > A[i]:
                    return 1
    return 0

A=list(map(int,input().split()))
print(solution(A))
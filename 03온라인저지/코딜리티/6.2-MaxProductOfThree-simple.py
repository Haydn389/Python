import sys
input=sys.stdin.readline

def solution(A):
    A.sort()
    multi1=A[0]*A[1]*A[-1]
    multi2=A[-1]*A[-2]*A[-3]
    return max(multi1,multi2)

A=list(map(int,input().split()))
print(solution(A))
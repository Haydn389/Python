import sys
input=sys.stdin.readline
#반복문사용하지 않고 총합 계산해서 빼기
def solution(A):
    n=len(A)+1
    return n*(n+1)//2 - sum(A)

A=list(map(int,input().split()))
print(solution(A))
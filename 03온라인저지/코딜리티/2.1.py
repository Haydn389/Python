import sys
input=sys.stdin.readline

def solution(A,K):
    from collections import deque
    d=deque(A)
    d.rotate(K)
    return  list(d)
A=list(map(int,input().split()))
K=int(input())
print(solution(A,K))
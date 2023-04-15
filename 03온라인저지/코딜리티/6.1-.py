import sys
input=sys.stdin.readline

def solution(A):
    s=set()
    for i in A:
        s.add(i)
    return  len(list(s))

A=list(map(int,input().split()))
print(solution(A))
import sys
input=sys.stdin.readline

def solution(A):
    m1=max(A)
    if m1<=0:
        return 1
    s=set(list(range(1,m1+1)))
    s=s-set(A)
    if len(s)==0:
        return m1+1
    return min(list(s))
A=list(map(int,input().split()))
print(solution(A))
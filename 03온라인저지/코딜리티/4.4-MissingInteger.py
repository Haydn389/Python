import sys
input=sys.stdin.readline

def solution(A):
    A=sorted(A)
    if A[-1]<1:
        return 1
    pre=0   
    for i in A:
        if i==pre or i<1:#같은 값 반복되는 경우 or 1보다 작은경우
            continue
        if i-pre==1 or pre<0:#음수인 경우 or 차이가 1만큼 나는경우
            pre=i
        if i-pre>1:
            return pre+1
    return pre+1

A=list(map(int,input().split()))
print(solution(A))
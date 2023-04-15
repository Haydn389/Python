import sys
input=sys.stdin.readline
#존재여부를 set 자료형과의 차집합으로 계산
def solution(A):
    S=set(list(range(1,len(A)+1)))
    A=set(A)
    # print(S)
    # print(A)
    # print(S-A)

    if len(S-A)==0:
        return 1
    return 0

A=list(map(int,input().split()))
print(solution(A))
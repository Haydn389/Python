import sys
input=sys.stdin.readline
#set자료형의 차집합을 활용하여 계산
def solution(X,A):
    s=set(list(range(1,X+1)))
    # print(A)
    # print(s)
    for i,a in enumerate(A):
        s-=set([a])
        if len(s)==0:
            return i
        # print(len(s),s,i)
    return -1   ##예외처리 -1 주의!!

X=int(input())
A=list(map(int,input().split()))
print(solution(X,A))
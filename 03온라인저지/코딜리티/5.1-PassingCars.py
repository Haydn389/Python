import sys
input=sys.stdin.readline

def solution(A):
    zero=0
    cnt=0
    for i in A:
        if i==0:
            zero+=1
        else:
            cnt+=zero*i
    
    return -1 if cnt>1e9 else cnt

A=list(map(int,input().split()))
print(solution(A))
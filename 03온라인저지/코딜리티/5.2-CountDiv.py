import sys
input=sys.stdin.readline

def solution(A,B,K):
    import math
    # cnt=0
    # for i in range(A,B+1):
    #     if i%2==0:
    #         cnt+=1
    # print(math.floor(B/K))
    # print(math.ceil(A/K))
    return math.floor(B/K)-math.ceil(A/K)+1

A,B,K=map(int,input().split())
print(solution(A,B,K))
import sys
input=sys.stdin.readline

def solution(A):
    import sys
    #3 2 -6 4 0
    partSum=0
    maxSum=-sys.maxsize
    for i in A:
        maxSum=max(maxSum,partSum+i)
        partSum=max(0,partSum+i)
    return maxSum

A=list(map(int,input().split()))
print(solution(A))
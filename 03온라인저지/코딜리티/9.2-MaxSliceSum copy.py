import sys
input=sys.stdin.readline

def solution(A):
    import sys
    maxSum=-sys.maxsize
    partSum=0
    for i in A:
        maxSum=max(maxSum,partSum+i)
        partSum=max(0,partSum+i)

    return maxSum



A=list(map(int,input().split()))
print(solution(A))
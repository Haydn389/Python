import sys
input=sys.stdin.readline

def solution(X,Y,D):
    import math
    ans = math.ceil((Y-X)/D)
    return ans

X,Y,D=list(map(int,input().split()))
print(solution(X,Y,D))
import sys
input=sys.stdin.readline
#부분합 사용
def solution(A):
    n=len(A)
    s=[0]*(n+1)
    res=[]
    for i in range(n):
        s[i+1]=s[i]+A[i]
    for j in range(1,n):
        res.append(abs(s[j]-(s[n]-s[j])))
    # print(res)
    return min(res)

A=list(map(int,input().split()))
print(solution(A))
import sys
input=sys.stdin.readline
#idea : Array의 평균은 subArray의 평균과 같거나 크다
#따라서 가장 작은 sub array인 2에대해서만 검토하면 된다
#다만 홀 수 인 경우를 고려하여 2,3까지 검사
def solution(A):
    import sys
    n=len(A)
    s=[0]*(n+1)
    for k in range(n):
        s[k+1]=s[k]+A[k]
    min_v=sys.maxsize
    i,j=1,2
    min_idx=i
    while(j<=n):
        res=(s[j]-s[i-1])/2
        if min_v > res:
            min_v=res
            min_idx=i
        i+=1
        j+=1

    i,j=1,3
    while(j<=n):
        res=(s[j]-s[i-1])/3
        if min_v > res:
            min_v=res
            min_idx=i
        i+=1
        j+=1

    return min_idx-1

A=list(map(int,input().split()))
print(solution(A))
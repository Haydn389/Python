import sys
input=sys.stdin.readline

def solution(A):
    import sys
    A.sort()
    idx=0
    for i in range(len(A)):
        if 0 < A[i]:
            idx=i
            break
    left=A[:idx]
    right=A[idx:]
    sum=-sys.maxsize
    if len(right)>=3:
        sum=max(sum,right[-1]*right[-2]*right[-3])
    if len(left)>=2:
        sum=max(sum,left[0]*left[1]*right[-1])
    else:
        sum=max(sum,A[-1]*A[-2]*A[-3])


    print(left,right)
    return sum

A=list(map(int,input().split()))
print(solution(A))
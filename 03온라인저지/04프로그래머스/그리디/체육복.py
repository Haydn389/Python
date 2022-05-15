import sys

n=int(sys.stdin.readline().strip())

lost=list(map(int,sys.stdin.readline().split()))
reserve=list(map(int,sys.stdin.readline().split()))


def solution(n, lost, reserve):
    cur=[1]*(n+1)
    for i in lost:
        cur[i-1]-=1

    for j in reserve:
        if cur[j-1]==0:
            cur[j-1]=1

        elif cur[(j-1)-1]==0:
            cur[(j-1)-1]=1
            if j==n:continue
        elif cur[(j-1)+1]==0:
            cur[(j-1)+1]=1
        else:
            continue
    print(cur)
    return sum(cur)-1


print(solution(n, lost, reserve))
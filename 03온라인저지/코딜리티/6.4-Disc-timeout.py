import sys
input=sys.stdin.readline

#idea 
def solution(A):
    cnt=0
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            temp1= i+A[i]
            temp2=j-A[j]
            if temp2<=temp1:
                cnt+=1

    return cnt

A=list(map(int,input().split()))
print(solution(A))
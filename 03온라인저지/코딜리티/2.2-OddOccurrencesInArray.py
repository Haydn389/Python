import sys
input=sys.stdin.readline

def solution(A):
    res={}
    for i in A:
        if i not in res:
            res[i]=1
        else:
            res[i]+=1
    for k,v in res.items():
        if v%2==1:
            return k
A=list(map(int,input().split()))
print(solution(A))
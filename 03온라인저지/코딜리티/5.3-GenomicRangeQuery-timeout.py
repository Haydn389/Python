import sys
input=sys.stdin.readline

def solution(S,P,Q):
    d={'A':1,'C':2,'G':3,'T':4}
    # print(list(S))
    a=[]
    res=[]
    for i in S:
        a.append(d[i])
    print(a)
    for i in range(len(P)):
        res.append(min(a[P[i]:Q[i]+1]))
    return  res
S=input().rstrip()
P=list(map(int,input().split()))
Q=list(map(int,input().split()))
print(solution(S,P,Q))
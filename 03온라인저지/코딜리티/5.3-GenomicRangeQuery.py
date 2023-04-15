import sys
input=sys.stdin.readline

def solution(S,P,Q):
    # d={'A':1,'C':2,'G':3,'T':4}
    res=[]
    for i in range(len(P)):
        A=P[i]
        B=Q[i]
        min_v=4
        if 'A' in S[A:B+1]:
            min_v=1
        elif 'C' in S[A:B+1]:
            min_v=2
        elif 'G' in S[A:B+1]:
            min_v=3

        res.append(min_v)
    return  res
S=input().rstrip()
P=list(map(int,input().split()))
Q=list(map(int,input().split()))
print(solution(S,P,Q))
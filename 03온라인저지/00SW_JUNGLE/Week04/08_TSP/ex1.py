import sys
input=sys.stdin.readline
n=int(input())
inf=sys.maxsize
w=[[-1]*(n+1)]
for _ in range(n):
    w.append([-1]+list(map(int,input().split())))
for i in range(1,n+1):
    for j in range(1,n+1):
        if w[i][j]==0: w[i][j]=inf
def isIn(i,A):
    if A&(1<<(i-2))!=0:
        return True
    else:
        return False

def diff(A,j):
    t=1<<(j-2)
    return A&(~t)

def count(A,n):
    cnt=0
    for i in range(n-1):
        if A&(1<<(i))!=0:
            cnt+=1
    return cnt

def minimum(W,D,i,A):
    min_val=inf
    min_j=1
    n=len(W)-1
    for j in range(2,n+1):
        if isIn(j,A):
            m=W[i][j]+D[j][diff(A,j)]
            if m<min_val:
                min_val=m
                min_j=j
    return min_val,min_j



def tsp(W):
    n=len(W)-1 #n=8
    size=2**(n-1)
    D=[[0]*size for _ in range(n+1)]
    P=[[0]*size for _ in range(n+1)]
    for i in range(2,n+1):
        D[i][0]=W[i][1]
    for k in range(1,n-1): #1~6
        for A in range(1,size-1):
            if count(A,n)==k:
                for i in range(2,n+1):
                    if not isIn(i,A):
                        D[i][A],P[i][A]=minimum(W,D,i,A)
    A=size-1
    D[1][A],P[1][A]=minimum(W,D,1,A)
    return D,P

D,P=tsp(w)
print(D[1][2**(n-1)-1])


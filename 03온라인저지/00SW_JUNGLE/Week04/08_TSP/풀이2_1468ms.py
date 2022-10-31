import sys
input=sys.stdin.readline

n=int(input().strip())

A=[]
for i in range(n):
    A.append(list(map(int,input().strip().split())))


dp=list([0]*(1<<n-1)for _ in range(n))

def tsp(now, route):
    if dp[now][route] != 0:
        return dp[now][route]
    if route==(1<<n-1)-1:
        if A[now][0]:
            return A[now][0]
        return sys.maxsize
    
    answer=sys.maxsize
    for next in range(1,n):
        if A[now][next]==0:
            continue
        if route & 1<<(next -1):
            continue

        cost=A[now][next]+tsp(next,route|(1<<next-1))         
        if answer>cost:
            answer=cost
    dp[now][route]=answer    
    
    return answer

print(tsp(0,0))
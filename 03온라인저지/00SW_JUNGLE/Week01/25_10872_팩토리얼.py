n=int(input())
def solve(n):
    if (n==1)or(n==0):return 1
    return n*solve(n-1)
print(solve(n))
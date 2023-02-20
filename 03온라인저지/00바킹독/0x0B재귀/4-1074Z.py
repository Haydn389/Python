import sys
input=sys.stdin.readline

n,r,c=map(int,input().split())

#n,r,c가주어졌을 대 가장 큰 
def func(n,r,c):
    if n==0:
        return 0
    half=2**(n-1)
    if r < half and c< half:
        return func(n-1,r,c)
    elif r < half and c>= half:
        return half**2+func(n-1,r,c-half)
    elif r >= half and c< half:
        return half**2*2+func(n-1,r-half,c)
    else:
        return half**2*3+func(n-1,r-half,c-half)

print(func(n,r,c))
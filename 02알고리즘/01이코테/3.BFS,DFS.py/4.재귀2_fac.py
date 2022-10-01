#반복적으로 구현한 n!
def fac(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return res
print(fac(5))

#재귀적으로 구현 n!

def fac2(n):
    if n<=1:
        return 1
    else:
        return n*fac2(n-1)
print(fac2(5))
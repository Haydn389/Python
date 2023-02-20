# a^b % m 을 구하라
a,b,m=map(int,input().split())
ans=0
def func(a,b,m):
    val=1
    while (b>0):
        val=val*a%m
        b-=1
    return val
print(func(a,b,m))
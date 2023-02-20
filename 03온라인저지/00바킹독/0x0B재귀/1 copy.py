# a^b % m 을 구하라
a,b,m=map(int,input().split())

##오버플로우 발생
def func(a,b,m):
    res=1
    while(b>0):
        res*=a
        b-=1
    return res%m

##개선) 나머지 값만을 가지고 간다
def func1(a,b,m):
    res=1
    while(b>0):
        res=res*a%m
        b-=1
    return res

print(func(a,b,m))
t= int(input())


def solve(n):
    #n==1
    #n==2,3
    #나머지
    if n==1:return False
    if 1<=n<=3:
        return True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return True
    return False



for _ in range(t):
    num=int(input())
    a=b=num//2
    while a>0:
        if solve(a) and solve(b):
            print(a,b)
            break
        a-=1
        b+=1
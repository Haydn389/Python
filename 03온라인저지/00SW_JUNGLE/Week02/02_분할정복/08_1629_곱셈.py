import sys
input=sys.stdin.readline
a,b,c=list(map(int,input().split()))
# a,b,c=10,11,12

#idea
# a=15
# b=7
# print(a*a*a%b)
# print(((a%b)*(a%b)*(a%b))%b)

def sol(a,b,c):
    # global c
    if b==1:
        return a%c
    if b%2==0:
        return (sol(a,b//2,c)**2)%c
    else:
        return ((sol(a,b//2,c)**2)*a)%c


print(sol(a,b,c))
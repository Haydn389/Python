# https://guccin.tistory.com/m/69

import sys
input=sys.stdin.readline
a,b,c=list(map(int,input().split()))

def sol(a,b):
    global c
    if b==1:
        return a%c
    
    if b%2==0:
        return (sol(a,b//2)*sol(a,b//2))%c
    else:
        return ((sol(a,b//2)*sol(a,b//2))*a)%c


print(sol(a,b))
import sys
input=sys.stdin.readline

a,b,c=map(int,input().split())

def func(a,b,c):
    if b==1:
        return a%c
    temp = func(a,b//2,c)
    temp=temp*temp%c
    if b%2==0:
        return temp
    else:
        return temp*a%c

print(func(a,b,c))
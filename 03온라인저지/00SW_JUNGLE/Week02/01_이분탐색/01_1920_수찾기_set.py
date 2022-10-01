import sys
input=sys.stdin.readline

n= int(input())
a=set(map(int,input().split()))
t= int(input())
keys=list(map(int,input().split()))

for key in keys:
    if key in a:
        print("1")
    else:
        print("0")
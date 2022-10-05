import sys
input=sys.stdin.readline

n= int(input())
a=list(map(int,input().split()))
a.sort()
t= int(input())

keys=list(map(int,input().split()))

def bin(a,key):
    pl=0
    pr=len(a)-1
    while pl<=pr:
        mid=(pr+pl)//2
        if a[mid]==key:
            print(1)
            return
        elif a[mid]<key:
            pl=mid+1
        else:
            pr=mid-1
    print(0)
    return

for key in keys:
    bin(a,key)
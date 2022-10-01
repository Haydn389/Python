import sys
input=sys.stdin.readline

n= int(input())
a=list(map(int,input().split()))
a.sort()
# a=sorted(a)
t= int(input())

def bin_search(a,key):
    pl=0
    pr=len(a)-1
    while True:
        pc=(pr+pl)//2
        if a[pc]==key:
            return 1
        elif a[pc]<key:
            pl=pc+1
        else:
            pr=pc-1
        if pr<pl:
            break
    return 0

keys=list(map(int,input().split()))

for key in keys:
    print(bin_search(a,key))

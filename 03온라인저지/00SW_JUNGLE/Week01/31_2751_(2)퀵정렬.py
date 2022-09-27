#퀵정렬
import sys
t = int(sys.stdin.readline())
a=[]
for _ in range(t):
    a.append(int(sys.stdin.readline()))


def quick(a,left,right):
    pr=right
    pl=left
    x=a[(left+right)//2]
    while pl<=pr:
        while a[pr]>x:pr-=1
        while a[pl]<x:pl+=1
        if pl<=pr:
            a[pr],a[pl]=a[pl],a[pr]
            pr-=1
            pl+=1

    if left<pr:quick(a,left,pr)
    if pl<right:quick(a,pl,right)

# a=[1,3,9,4,7,8,6]
quick(a,0,len(a)-1)
# print(a)
for i in a: print(i)

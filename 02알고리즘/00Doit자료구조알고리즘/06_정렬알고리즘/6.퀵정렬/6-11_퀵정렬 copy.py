from pydoc import plain


def q(a,left,right):
    pl=left
    pr=right
    x=a[(left+right)//2]

    while pl<=pr:
        while a[pr]>x:pr-=1
        while a[pl]<x:pl+=1
        if pl<=pr:
            a[pr],a[pl]=a[pl],a[pr]
            pr-=1
            pl+=1
    if left<pr:q(a,left,pr)
    if pl<right:q(a,pl,right)



a=[7,5,9,0,3,1,6,2,4,8]

q(a,0,len(a)-1)
print(a)

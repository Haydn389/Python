array = [7,5,9,0,3,1,6,2,4,8]
# array=[5,8,4,2,6,1,3,9,7]

def qsort(array, left, right):
    pl=left
    pr=right
    x=array[(left+right)//2]

    while pl<=pr:
        while array[pl]<x:pl+=1
        while array[pr]>x:pr-=1
        if pl<=pr:
            array[pl],array[pr]=array[pr],array[pl]
            pl+=1
            pr-=1
    if (left<pr) : qsort(array,left,pr)
    if (pl<right) : qsort(array,pl,right)

qsort(array,0,len(array)-1)
print(array)

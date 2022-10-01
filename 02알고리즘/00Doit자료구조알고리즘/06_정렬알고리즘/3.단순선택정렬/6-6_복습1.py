a=[6,4,8,3,1,9,7]
# a=[9,1,2,3,4,5,6]

def select(a):
    pass
    n=len(a)
    for i in range(n):
        min_i=i
        for j in range(i,n):
            if a[i]>a[j]:
                min_i=j
        a[i],a[min_i]=a[min_i],a[i]


select(a)
print(a)
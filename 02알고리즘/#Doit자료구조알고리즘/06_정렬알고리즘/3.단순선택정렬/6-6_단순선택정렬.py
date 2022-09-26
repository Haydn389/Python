a=[6,4,3,7,1,9,8]
a=[5,8,4,6,7,2,1]
cnt=0
def select(a):
    global cnt
    n=len(a)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            cnt+=1
            print(a)
            if a[min]>a[j]:
                min=j
            a[i],a[min]=a[min],a[i]


select(a)
print(a)
print(cnt)
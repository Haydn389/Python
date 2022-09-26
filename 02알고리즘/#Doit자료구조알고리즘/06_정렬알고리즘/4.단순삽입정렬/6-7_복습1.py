# a=[1,4,6,7,3,9,8]
a=[6,4,1,7,3,9,8]
cnt=0
def straight_insertion_sort(a):
    n=len(a)
    for i in range(n):
        temp=a[i]
        j=i
        while j>0 and a[j-1]>temp:
            a[j]=a[j-1]
            j-=1

        a[i]=temp
straight_insertion_sort(a)
print(a)
print(cnt)
a = [9, 4, 1, 7, 6, 8, 3, 5, 2]
cnt = 0


def straight_insertion_sort(a):
    n = len(a)
    h=n//2
    while h>0:
    ###################
        for i in range(h,n):
            temp=a[i]
            j=i-h
            while j>=0 and a[j]>temp:
                a[j+h]=a[j]
                j-=h
            a[j+h]=temp
    ###################
        h//=2
        

straight_insertion_sort(a)
print(a)
# print(cnt)

# a=[1,4,6,7,3,9,8]
a=[6,4,1,7,3,9,8]
a=[9,4,1,7,6,8,3,5,2]
cnt=0
def straight_insertion_sort(a):
    global cnt
    n=len(a)
    for i in range(1,n): #i=1~6
        for j in range(i,0,-1):
            if a[j-1]>a[j]:
                a[j],a[j-1]=a[j-1],a[j]
                cnt+=1
            else: break

straight_insertion_sort(a)
print(a)
print(cnt)

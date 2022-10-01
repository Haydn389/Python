from typing import MutableSequence

# a=[6,4,3,7,1,9,8]
a=[9,1,3,4,6,7,8] #셰이커정렬
a=[6,4,1,7,3,9,8]
a=[9,4,1,7,6,8,3,5,2]
cnt=0
def bubble_sort(a:MutableSequence) ->None:
    global cnt
    n=len(a) #n=7
    for i in range(n-1): #** i =0,1,2,3,4,5 즉 n-1인 6번 반복됨 
        for j in range(n-1,i,-1): #j = 
            if a[j-1] > a[j]:
                a[j-1], a[j]=a[j],a[j-1]
                cnt+=1


bubble_sort(a)

print(a)
print(cnt)





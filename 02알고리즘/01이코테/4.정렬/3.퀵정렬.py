# array = [7,5,9,0,3,1,6,2,4,8]
array = [2,4,3]

def quick(array,start,end):
    if start>=end:
        return
    pivot=start
    left=start+1
    right=end
    while(left<=right):
        while(left<=end and array[pivot]>=array[left]):
            left+=1
        while(start<right and array[pivot]<=array[right]):
            right-=1
        if left>right:
            array[pivot],array[right]=array[right],array[pivot]            
        else:
            array[left],array[right]=array[right],array[left]
    quick(array,start,right-1)
    quick(array,right+1,end)


quick(array,0,len(array)-1)
print(array)










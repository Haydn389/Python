def binary(array, target, start, end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]<target:
            start=mid+1
        else: 
            end=mid-1


    return None



n,target=list(map(int,input().split()))
array=list(map(int,input().split()))

res=binary(array,target,0,n-1)
if res==None:
    print("없음")
else: print(res+1)
n,target=list(map(int,input().split()))

array=list(map(int,input().split()))

def bi_sear(array,target,start,end):
    while start<=end:
        mid = (start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None

result=bi_sear(array,target,0,n-1)

if result==None:
    print("없음")
else: print(result+1)
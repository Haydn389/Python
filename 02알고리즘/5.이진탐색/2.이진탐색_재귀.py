n,target=list(map(int,input().split()))

array=list(map(int,input().split()))

def bi_sear(array,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    # print(mid)
    if array[mid]==target:
        return mid
    elif array[mid]>=target:
        return bi_sear(array,target,start,mid)
    else:
        return bi_sear(array,target,mid+1,end)

result=bi_sear(array,target,0,n-1)

if result==None:
    print("없음")
else: print(result+1)
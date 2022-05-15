import sys

n,target=map(int,sys.stdin.readline().split())

array=list(map(int,sys.stdin.readline().split()))

start=0
end=max(array)
res=0
while(start<=end):
    tot=0
    mid=(start+end)//2
    for i in array:
        if i>mid:
            tot+=i-mid
    if tot > target:
        start=mid+1
    else:
        res=mid
        end=mid-1

print(res)


import sys
n1 = int(sys.stdin.readline())
data1 = list(map(int,input().split()))    #int
data1.sort()

n2 = int(sys.stdin.readline())
data2 = list(map(int,input().split()))    #int

def search(array,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return True
        elif array[mid]<target:
            start=mid+1
        else: 
            end=mid-1
    # return None


for i in data2:
    if search(data1,i,0,n1-1)==True:
        print("yes",end=" ")
    else: print("no",end=" ")

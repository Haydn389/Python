import sys

input=sys.stdin.readline
n=int(input())
a=list(map(int,sys.stdin.readline().split()))
a.sort()

idx=n-1
k=a[idx]

cnt=0
while (idx>=0):   
    i=0
    j=n-1
    sum=a[i]+a[j]
    while(i!=j):
        # if (a[i]==k):
        if (i==idx):
            i+=1
            sum=a[i]+a[j]
        # elif (a[j]==k):
        elif (j==idx):
            j-=1
            sum=a[i]+a[j]
        elif sum>k:
            j-=1
            sum=a[i]+a[j]
        elif sum<k:
            i+=1
            sum=a[i]+a[j]
        else:
            # print(sum)
            cnt+=1
            break
    idx-=1
    k=a[idx]
# print('=======')
print(cnt)





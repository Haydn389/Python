import sys

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
a=list(map(int,input().split()))

a.sort()

start=0
end=n-1
cnt=0
sum=a[start]+a[end]
while(start!=end):
    if sum==m:
        cnt+=1
        start+=1
        sum=a[start]+a[end]

    elif sum > m:
        end-=1
        sum=a[start]+a[end]

    else:
        start+=1
        sum=a[start]+a[end]

# print('-----')
print(cnt)
import sys

input=sys.stdin.readline
n=int(input())
a=list(map(int,sys.stdin.readline().split()))
a.sort()

idx=n-1
target=a[idx]
cnt=0
while (idx>=0):   
    i=0
    j=n-1
    sum=a[i]+a[j]
    while(i!=j):
        #target값의 idx와 i가 같거나 sum이 target보다 작으면 i++
        if i==idx or sum<target:
            i+=1
        #target값의 idx와 j가 같거나 sum이 target보다 크면 j--
        elif j==idx or sum>target:
            j-=1
        #target과 sum이 같으면 cnt++
        else:
            cnt+=1
            break
        sum=a[i]+a[j]
    idx-=1
    target=a[idx]
print(cnt)





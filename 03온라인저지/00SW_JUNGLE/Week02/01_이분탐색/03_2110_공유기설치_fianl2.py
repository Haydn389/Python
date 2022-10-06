import sys
input = sys.stdin.readline
n, key = map(int, input().split())
a = list(int(input()) for _ in range(n))
a.sort()

pl=1
pr=a[-1]-a[0]
ans=0
while pl<=pr:
    mid=(pl+pr)//2
    cnt=1
    start=a[0]
    for i in range(1,n):
        if a[i]-start>=mid:
            cnt+=1
            start=a[i]
    if cnt<key:
        pr=mid-1
    else:
        pl=mid+1
        ans=mid
print(ans)
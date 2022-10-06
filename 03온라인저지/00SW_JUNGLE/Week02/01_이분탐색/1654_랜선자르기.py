import sys
input = sys.stdin.readline
n,key = map(int,input().split())
a= sorted(list(int(input()) for _ in range(n)))
# n,key=4, 11
# a=[457, 539, 743, 802]

pl=1
pr=a[-1]
pr=sum(a)//n
while pl<=pr:
    mid=(pl+pr)//2
    # if mid==0:break
    cnt=0
    for i in a:
        cnt+=(i//mid)
    if cnt>=key:
        pl=mid+1
        res=mid
    else:
        pr=mid-1

print(res)


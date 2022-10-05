import sys
input = sys.stdin.readline
n,m = map(int,input().split())
a = list(map(int, input().split()))

pl=0
pr=max(a)
res=0
while pl<=pr:
    mid=(pl+pr)//2
    tot=0
    for i in a:
        if i>mid:
            tot+=i-mid
    if m <= tot:
        res=mid
        pl=mid+1
    else:
        pr=mid-1
print(res)

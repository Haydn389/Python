import sys
input = sys.stdin.readline
n,k = map(int,input().split())
a= sorted(list(int(input()) for _ in range(n)))

# print(n,m)
# print(a)
pl=a[0]
# pr=a[-1]+k
pr=pl+k

res=0
while pl <= pr:
    mid=(pl+pr)//2
    tot=0
    for i in a:
        if i<mid:
            tot+=mid-i
    if k<tot:
        pr=mid-1
    else:
        pl=mid+1
        res=mid

print(res)

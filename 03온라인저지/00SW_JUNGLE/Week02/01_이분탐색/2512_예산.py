import sys
input = sys.stdin.readline
n = int(input())
a = sorted(list(map(int, input().split())))
key = int(input())

pl=0
pr=a[-1]

while pl<=pr:
    mid=(pl+pr)//2
    cnt=0
    for i in a:
        if i<mid:
            cnt+=i
        else:
            cnt+=mid
    if key < cnt:
        pr=mid-1
    else:
        pl=mid+1
        res=mid

print(res)
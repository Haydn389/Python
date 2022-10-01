import sys 
n,k=list(map(int,input().split()))
a=[]
for _ in range(n):
    a.append(int(sys.stdin.readline()))

# n,k=3,10
# a=[10, 20, 15]

a.sort()
pl=a[0]
# pr=a[-1]
pr=a[-1] #만약 a의 값들이 모두 같거나 비슷한경우 안됨

res=0
while pl<=pr:
    mid=(pl+pr)//2
    tot=0
    for x in a:
        if mid>x:
            tot+=mid-x
    if tot > k:
        pr=mid-1
    else:
        res=mid
        pl=mid+1

print(res)



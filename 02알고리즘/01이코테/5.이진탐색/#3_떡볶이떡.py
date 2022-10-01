# n,m=list(map(int,input().split()))
# a=list(map(int,input().split()))
n, m = 4, 6
a = [19, 15, 10, 17]

pl = 0
pr = max(a)

res = 0
while (pl <= pr):
    tot = 0
    mid = (pl+pr)//2
    for i in a:
        if i > mid:
            tot += (i-mid)
    if tot<m:
        pr=mid-1
    else:
        res=mid
        pl=mid+1
    

        

print(res)

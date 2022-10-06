import sys
input = sys.stdin.readline

n, m, l = list(map(int, sys.stdin.readline().split()))
p = sorted(list(map(int, sys.stdin.readline().split())))
a=list((map(int,input().split())) for _ in range(m))

cnt=0


for x,y in a:
    if y>l:
        continue
    pl=0
    pr=n-1
    p_max=x+(l-y)
    p_min=x-(l-y)
    while pl<=pr:
        mid=(pl+pr)//2
        if p_min<=p[mid]<=p_max:
            cnt+=1
            break
        elif p[mid]<p_min:
            pl=mid+1
        else:
            pr=mid-1
print(cnt)
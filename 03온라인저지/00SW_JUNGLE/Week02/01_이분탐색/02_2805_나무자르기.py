import sys 
n,m=list(map(int,input().split()))
a=list(map(int,input().split()))
# n, m = 4, 6
# a = [19, 15, 10, 17]

res=0
pl=0
pr=max(a) #pr에는 리스트의 길이가 아닌 입력받은 값중 가장 큰값을 넣는다

while(pl<=pr):
    mid=(pl+pr)//2
    tot=0
    for x in a:
        if x>mid:
            tot+=(x-mid)
    if tot<m:
        pr=mid-1
    else:
        res=mid
        pl=mid+1

print(res)
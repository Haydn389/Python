import sys

# n,key=list(map(int,sys.stdin.readline().split()))
# a=list(map(int,sys.stdin.readline().split()))

n,key=4,7
a=[20,15,10,17]

pl=0
pr=max(a)
res=0
while pl <=pr:
    print("진입 start:{},end:{}".format(pl,pr))
    mid=(pr+pl)//2
    tot=0
    for i in a:
        if i-mid>0:
            tot+=i-mid
    print('mid', mid)
    print(f'sum = {tot}')
    if tot<key:
        pr=mid-1
        print(f'{key} 미만 start=', pl, 'end=', pr, '\n')
    else:
        res=mid
        pl=mid+1
        print(f'{key} 이상 start=', pl, 'end=', pr, '\n')
        print("res",res)
    print("-"*50)
print(pr)
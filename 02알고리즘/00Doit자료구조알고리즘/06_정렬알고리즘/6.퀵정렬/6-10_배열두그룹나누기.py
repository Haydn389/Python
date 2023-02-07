cnt=0
def partition(a):
    n=len(a)
    pl=0
    pr=n-1
    x=a[n//2]
    while pl<=pr:
        while a[pl]<x:
            pl+=1
        while a[pr]>x:
            pr-=1
        if pl<=pr: #위에서 pl,pr 증감을 수행했으므로 교차했는지 검사
            #이미 교차했으면 서로 값을 바꿀 필요가 없음
            a[pl],a[pr]=a[pr],a[pl]
            pl+=1
            pr-=1
    print(pl,pr)
# a=[1,8,7,4,5,2,6,3,9]
# a=[9,4,1,7,6,8,3,5,2]
# a=[5,8,4,2,6,1,3,9,7]
a=[1,4,3,7,8,6,5]

partition(a)
print(a)
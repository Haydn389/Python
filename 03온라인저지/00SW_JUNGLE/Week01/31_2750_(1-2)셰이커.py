import sys
t = int(sys.stdin.readline())
a=[]
for _ in range(t):
    a.append(int(sys.stdin.readline()))
# a=[9,7,5,1,4,6,8]
#
def shaker_sort(a):
    n=len(a)
    left=0
    right=n-1
    last=right
    while left<right:
        for j in range(right,left,-1):
            if a[j-1]>a[j]:
                a[j-1],a[j]=a[j],a[j-1]
                last=j
        left=last
        for j in range(left,right):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                last=j
        right=last
        


shaker_sort(a)
for i in a: print(i)

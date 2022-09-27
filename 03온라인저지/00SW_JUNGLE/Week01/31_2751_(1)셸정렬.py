import sys

t = int(sys.stdin.readline())
a=[]
for _ in range(t):
    a.append(int(sys.stdin.readline()))


def shell(a):
    n=len(a)
    h=1
    while h < n//9:
        h=h*3+1
    while h>0:
        for i in range(h,n):
            temp=a[i]
            j=i-h
            while j>=0 and a[j]>temp:
                a[j+h]=a[j]
                j-=h
            a[j+h]=temp
        h//=2
# a=[1,3,9,4,7,8,6]
shell(a)
# print(a)
for i in a: print(i)

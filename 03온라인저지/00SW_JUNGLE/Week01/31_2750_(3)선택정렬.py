import sys

t = int(sys.stdin.readline())
a=[]
for _ in range(t):
    a.append(int(sys.stdin.readline()))

#
def select(a):
    n=len(a)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if a[min]>a[j]:
                min=j
        a[min],a[i]=a[i],a[min]

select(a)
for i in a: print(i)

import sys

t = int(sys.stdin.readline())
a=[]
for _ in range(t):
    a.append(int(sys.stdin.readline()))

def bubble_sort(a):
    n=len(a)
    for i in range(n):
        for j in range(n-1,i,-1):
            if a[j-1]>a[j]:
                a[j-1],a[j]=a[j],a[j-1]

bubble_sort(a)
for i in a: print(i)

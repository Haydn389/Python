import sys

# t = int(sys.stdin.readline())
# a=[]
# for _ in range(t):
#     a.append(int(sys.stdin.readline()))
a=[9,4,1,7,6,8,3,5,2]
def select(a):
    n=len(a)

    for i in range(n):
        min=i
        for j in range(i+1,n):
            if a[min]>a[j]:
                min=j
        a[i],a[min]=a[min],a[i]

select(a)
print(a)

# for i in a: print(i)

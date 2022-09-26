import sys
t = int(sys.stdin.readline())
a=[]
for _ in range(t):
    a.append(int(sys.stdin.readline()))
# a=[9,7,5,1,4,6,8]
#
def select(a):
    n=len(a)
    for i in range(n):
        temp=a[i]
        j=i
        while j>0 and a[j-1]>temp:
            a[j]=a[j-1]
            j-=1
        a[j]=temp
      

select(a)
# print(a)
for i in a: print(i)

import sys

sys.setrecursionlimit(10**9)

a=[]
while True:
    try:
        a.append(int(input()))
    except:
        break


def tree(s,e):
    if s>e:
        return

    mid=e+1

    for i in range(s+1,e+1):
        if a[s]<a[i]:
            mid=i
            break

    tree(s+1,mid-1)
    tree(mid,e)
    print(a[s])

tree(0,len(a)-1)
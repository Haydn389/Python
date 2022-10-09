import sys
from typing import Sequence
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def tree(a):
    n=len(a)
    if n<=1:
        return a
    for i in range(1,n):
        if a[0]<a[i]:
            return tree(a[1:i])+tree(a[i:])+[a[0]]
    return tree(a[1:])+[a[0]]

a=[]
while True:
    try:
        a.append(int(sys.stdin.readline()))
    except:
        break

# a=tree(a)
for i in tree(a):
    print(i)
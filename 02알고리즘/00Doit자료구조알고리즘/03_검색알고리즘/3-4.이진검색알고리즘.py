from typing import Any, Sequence 
import sys
a=[1,2,3,5,7,8,9]

def bin_search(a,key):
    pl=0
    pr=len(a)-1
    # break조건 a[pc]==key or pr<pl:
    while True:
        pc=(pr+pl)//2
        if a[pc]==key:
            return pc
        elif a[pc]<key:
            pl=pc+1
        else:
            pr=pc-1
        if pl>pr:
            break
    return -1
            
key=int(sys.stdin.readline().rstrip())
idx=bin_search(a,key)
if idx==-1:
    print("값이 없습니다.")
else:
    print(f"검색값은 x[{idx}]에 있습니다.")
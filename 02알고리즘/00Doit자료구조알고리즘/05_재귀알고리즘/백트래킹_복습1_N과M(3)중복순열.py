import sys
n, m = map(int, sys.stdin.readline().split())
pos=[0]*m
flag=[0]*n

def set(i):
    if i ==m:
        print(pos)
        return
    for j in range(n):
        pos[i]=j
        set(i+1)
set(0)
import sys

n,k=map(int,sys.stdin.readline().split())

cnt=0

while True:
    target=(n//k)*k
    cnt+=n-target
    n=target
    if n<=1:
        break
    cnt+=1
    n//=k


print(cnt-1)
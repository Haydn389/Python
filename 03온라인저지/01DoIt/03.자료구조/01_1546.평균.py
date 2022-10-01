import sys
n = int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))

print(sum(arr)/max(arr)*100/n)
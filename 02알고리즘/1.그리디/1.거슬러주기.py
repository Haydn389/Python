import sys

n = int(sys.stdin.readline().strip())

type=[500,100,50,10]
cnt=0

for i in type:
    cnt+=n//i
    n%=i

print(cnt)
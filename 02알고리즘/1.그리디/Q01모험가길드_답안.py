import sys
n = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))   #int

data.sort()
group=0
cnt=0
for i in data:
    group+=1
    if group>=i:
        cnt+=1
        group=0

print(cnt)

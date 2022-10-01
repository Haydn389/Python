import sys
n = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))   #int

data.sort()
group=[]
cnt=0
for i in range(len(data)):
    group.append(data[i])
    if len(group)>=data[i]:
        cnt+=1
        group.clear()

print(cnt)

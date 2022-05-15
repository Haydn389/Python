import sys
n,k = map(int,sys.stdin.readline().split())

data1 = list(map(int,sys.stdin.readline().split()))
data2 = list(map(int,sys.stdin.readline().split()))

data1.sort()
data2.sort(reverse=True)

for i in range(k):
    if data1[i]<data2[i]:
        data1[i],data2[i]=data2[i],data1[i]
        
print(sum(data1))
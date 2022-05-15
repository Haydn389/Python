import sys
a,b = map(int,sys.stdin.readline().split())
data=[]
for i in range(1,50):
    for _ in range(i):
        data.append(i)
    # data+=[i]*i

print(sum(data[a-1:b]))
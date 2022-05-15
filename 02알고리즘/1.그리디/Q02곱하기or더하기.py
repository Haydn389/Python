import sys
data = sys.stdin.readline().strip() #str
sum=0

old=int(data[0])
for i in range(1,len(data)):
    if old<=0 or int(data[i])<=0:
        old+=int(data[i])
    else:
        old*=int(data[i])


print(old)
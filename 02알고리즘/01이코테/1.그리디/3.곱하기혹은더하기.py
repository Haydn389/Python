import sys

data=list(map(int,sys.stdin.readline().strip()))

sum=data[0]

for i in range(1,len(data)):
    # print("계산전 sum",sum,"data[i]",data[i])
    if data[i]<=1 or sum<=1:
        sum+=data[i]
    else: 
        sum*=data[i]
    # print("계산후 sum",sum,"data[i]",data[i])
print(sum)


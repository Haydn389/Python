import sys

data=sys.stdin.readline().strip()
sum=0
aaa=[]
for i in data:
    if int(ord(i))<=57:
        sum+=int(i)
    else:
        aaa.append(i)

aaa.sort()
if sum!=0:
    aaa.append(str(sum))

print(''.join(aaa))


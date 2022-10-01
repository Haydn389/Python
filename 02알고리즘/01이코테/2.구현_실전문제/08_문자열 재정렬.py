import sys

s=sys.stdin.readline().strip()
res=[]
sum=0

for i in s:
    if i.isalpha():
        res.append(i)
    else:
        sum+=int(i)
res.sort()
# print(res)
# print(sum)
if sum!=0:
   res.append(str(sum))

print(''.join(res))

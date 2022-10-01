import sys
# n=sys.stdin.readline().rstip()
n='55'
if int(n)<10:
    n="0"+n

res=n
cnt=0
while True:
    temp=int(res[0])+int(res[1])
    res= res[-1]+str(temp)[-1]
    cnt+=1
    if res==n:
        break

print(cnt)
import sys
input=sys.stdin.readline
n=int(input())

d=[0]*(n+1)

d[0]=0
d[1]=0

for i in range(2,n+1):
    temp=[]
    temp.append(d[i-1]+1)
    if i%3==0:
        temp.append(d[i//3]+1)
    if i%2==0:
        temp.append(d[i//2]+1)
    d[i]=min(temp)

print(d[n])
    
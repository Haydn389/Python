import sys

data=sys.stdin.readline()
dx=[-2,-1,1,2,2,1,-1,-2]
dy=[1,2,2,1,-1,-2,-2,-1]
x=int(data[1])
y=int(ord(data[0]))-int(ord('a'))+1
cnt=0
for i in range(8):
    nx=x+dx[i]
    ny=y+dy[i]
    if (nx>=1 and ny>=1 and nx <= 8 and ny <= 8 ):
        cnt+=1

print(cnt)
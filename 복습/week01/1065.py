import sys
input = sys.stdin.readline  

a=int(input())
cnt=0
for i in range(1,a+1):
    if i<100:
        cnt+=1
    elif i<1000:
        s=list(map(int,str(i)))
        if s[2]-s[1]==s[1]-s[0]:
            cnt+=1

print(cnt)
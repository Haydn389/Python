import sys
input=sys.stdin.readline

n=int(input())
cnt=0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            num=str(i)+str(j)+str(k)
            if '3' in num:
                cnt+=1

print(cnt)
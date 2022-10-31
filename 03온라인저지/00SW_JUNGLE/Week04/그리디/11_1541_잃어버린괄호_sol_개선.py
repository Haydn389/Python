import sys
input=sys.stdin.readline
a=input().rstrip().split("-")

temp=map(int,a[0].split("+"))
ans=sum(temp)
for i in range(1,len(a)):
    plus=map(int,a[i].split("+"))
    ans-=sum(plus)

print(ans)
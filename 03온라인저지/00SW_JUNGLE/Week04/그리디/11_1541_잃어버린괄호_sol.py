import sys
input=sys.stdin.readline
a=input().rstrip().split("-")

# print(a)
temp=a[0].split("+")
ans=0
for t in temp:
    ans+=int(t)
for i in range(1,len(a)):
    # print(a[i])
    # print(eval(a[i]))
    temp=0
    plus=a[i].split("+")
    for p in plus:
        temp+=int(p)
    ans-=temp

print(ans)
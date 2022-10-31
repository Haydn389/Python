import sys
input=sys.stdin.readline

x=input().rstrip()
y=input().rstrip()
n,m=len(x),len(y)
# print(x,y)
a=[0]*m

for i in range(n):
    cnt=0
    for j in range(m):
        if cnt<a[j]:
            cnt=a[j]
        elif x[i]==y[j]:
            a[j]=cnt+1
    # print(a)

# print(a)
print(max(a))
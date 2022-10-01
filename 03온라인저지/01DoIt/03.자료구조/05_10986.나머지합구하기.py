import sys

n,m=map(int,sys.stdin.readline().split())

a=list(map(int,sys.stdin.readline().split()))
s=[0]*n
c=[0]*m
s[0]=a[0]
cnt=0

# for i in a:
#     temp+=i
#     s=temp

for i in range(1,n):
    s[i]=s[i-1]+a[i]

for i in range(n):
    r=s[i]%m
    if r==0:
        cnt+=1
    c[r]+=1

for i in c:
    # print("i",i)
    cnt+=(i*(i-1)//2)
    # print("#",cnt)

print(cnt)

# 틀린풀이
# for i in range(1,n+1):
#     for j in range(i,n+1):
#         # print("i={}, j={}".format(i,j))
#         # print(s[j]-s[i-1])
#         if (s[j]-s[i-1])%m==0:
#             cnt+=1
#     #         print(s[j]-s[i-1])
#     # print("*******")
# print(cnt)
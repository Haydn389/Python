# d=[0] *100
# d[1]=1
# d[2]=1
# n=99
# for i in range(3,n+1):
#     d[i]=d[i-1]+d[i-2]
# print(d[n])

n=int(input())
# d=[0] *(n+1)
# d[1]=1
# d[2]=1
# for i in range(3,n+1):
#     d[i]=d[i-1]+d[i-2]
# print(d[n])

d=[0] *(n)
d[0]=1
d[1]=1
for i in range(2,n):
    d[i]=d[i-1]+d[i-2]
print(d)
print(d[n-1])

#1 1 2 3 5 8 13 21 34
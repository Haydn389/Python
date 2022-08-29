import sys
n,m = map(int,sys.stdin.readline().split(" "))
arr = list(map(int,sys.stdin.readline().split()))
s=[*arr]
for i in range(1,len(arr)):
    s[i]=s[i-1]+arr[i]

# print(arr)
# print(s)

for _ in range(n):
    i,j = map(int, sys.stdin.readline().split())
    if i ==1:
        print(s[j-1])
    else:
        print(s[j-1]-s[i-2])
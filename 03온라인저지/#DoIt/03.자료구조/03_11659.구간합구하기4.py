import sys
n,m = map(int,sys.stdin.readline().split(" "))
arr = list(map(int,sys.stdin.readline().split()))
s=[0]*(len(arr)+1)



for i in range(n):
    s[i+1]=s[i]+arr[i]
# print(arr)
# print(s)

# 정답코드 
# s=[0]
# temp=0
# for i in arr:
#     temp+=i
#     s.append(temp)

# print(arr)
# print(s)

for _ in range(m):
    i,j = map(int, sys.stdin.readline().split())
    print(s[j]-s[i-1])

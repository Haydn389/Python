import sys
input=sys.stdin.readline
n,k=map(int,input().split())

coins=[]
for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

# print(coin)

cnt=0
for coin in coins:
    cnt+=k//coin
    k=k%coin
print(cnt)
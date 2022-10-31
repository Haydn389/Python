import sys
input=sys.stdin.readline
n,k=map(int,input().split())

coin=[]
for _ in range(n):
    coin.append(int(input()))

# coin.sort(reverse=True)

# print(coin)

cnt=0
while k>0:
    if coin[n-1]>k:
        n-=1
    else:
        cnt+=k//coin[n-1]
        k=k%coin[n-1]
        n-=1
    # print(k,n)
print(cnt)
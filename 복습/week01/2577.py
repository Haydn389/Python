import sys
input = sys.stdin.readline
sum=1
for _ in range(3):
    sum*=int(input())
res=[0]*10
for i in str(sum):
    res[int(i)]+=1
for x in res:
    print(x)
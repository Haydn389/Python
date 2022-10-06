import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(int(input()) for _ in range(n))
a.sort()  # [1,2,4,8,9]
# print(len(a))
# n,m=5 ,3
# a=[1, 2, 8, 4, 9]
pl = 1
pr = a[-1]-a[0]
res = 0
while pl <= pr:
    mid = (pl+pr)//2
    cnt = 1
    # while True:
    start = a[0]
    for i in range(1, len(a)):
        if a[i]-start >= mid:
            cnt += 1
            start = a[i]
    if cnt < m:
        pr = mid-1
    else:
        pl = mid+1
        res = mid
print(res)

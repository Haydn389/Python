# https://seohyun0120.tistory.com/entry/%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4LIS-%EC%99%84%EC%A0%84-%EC%A0%95%EB%B3%B5-%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC

# 12015번
import bisect
n=int(input())
a=list(map(int,input().split()))

res=[a[0]]

for i in range(n):
    if a[i]>res[-1]:
        res.append(a[i])
    else:
        idx=bisect.bisect_left(res,a[i])
        res[idx]=a[i]
print(res)
print(len(res))
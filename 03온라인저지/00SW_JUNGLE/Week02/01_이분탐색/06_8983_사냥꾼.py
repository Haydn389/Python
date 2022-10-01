# https://etst.tistory.com/194
# https://western-sky.tistory.com/140

import sys
input = sys.stdin.readline
n,m,l=list(map(int,sys.stdin.readline().split()))
p=list(map(int,sys.stdin.readline().split()))
a=list((map(int,input().split())) for _ in range(m))

# n, m, l = 4, 8, 4
# p = [6, 1, 4, 9]
# a = [[7, 2], [3, 3], [4, 5], [5, 1], [2, 2], [1, 4], [8, 4], [9, 4]]

p.sort()  # p=[1,4,6,9]
# a.sort(key=lambda x:x[0])

cnt = 0
for x, y in a:
    if (y > l):  # y좌표가 l보다큰경우 무시
        continue
    p_min = x-(l-y)  # 해당 동물을 잡을 수 있는 최소 사대 좌표
    p_max = x+(l-y)  # 해당 동물을 잡을 수 있는 최대 사대 좌표
    pl = 0  # 사대 좌표 중 최솟값의 index
    pr = n-1  # 사대 좌표 중 최댓값의 index
    while pl <= pr:
        mid = (pl+pr)//2
        if p_min <= p[mid] <= p_max:
            cnt += 1
            break
        elif p[mid] < p_min:  # p[mid] < p_min or p_max < p[mid]
            pl = mid+1
        else:
            pr = mid-1
print(cnt)

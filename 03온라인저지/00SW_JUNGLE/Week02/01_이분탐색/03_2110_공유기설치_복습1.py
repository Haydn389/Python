import sys
n, key = list(map(int, sys.stdin.readline().split()))
a = []
for _ in range(n):
    a.append(int(sys.stdin.readline().rstrip()))
a.sort()
# ***여기서 포인터는 두 집사이거리(gap)
pl = 1           # 두 집사이 거리가 가장 작은경우 gap=1
pr = a[-1]-a[0]  # ← gap이 가장 큰 경우
ans = 0
while pl <= pr:
    mid = (pr+pl)//2    # mid=는 이번 step에서의 gap을 의미
                        # 처음으로 gap=4일때, 이번 step에서 가능한 공유기 최대 설치갯수를 구해보자
    cnt = 1             # 먼저 처음에 하나 박아놓고
    value = a[0]
    for i in range(1, n):
        if a[i]-value >= mid:
            cnt += 1        # 갯수 하나 늘리고
            value = a[i]    # value를 새로 초기화
    if cnt < key:           # 이번에 시도한 gap에서, 요구되는 공유기 갯수보다 작으면
        pr = mid-1          # gap을 줄여서 다시시도
    else:                   # 이번에 시도한 gap에서, 요구되는 공유기 갯수 이상이면
        pl = mid+1          # gap을 늘려서 다시시도
        ans = mid
print(ans)

# https://nyeongnyeong.tistory.com/201

import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))

pl = 0
pr = n-1

res = sys.maxsize

while pl < pr:              # 둘이 같은 경우는 없으니 등호는 빼줌
    tot = a[pl]+a[pr]       # 합 계산
    if abs(tot) < res:      # res보다 작은경우 res업데이트
        res = abs(tot)
        ans = a[pl], a[pr]  # ans 없데이트
    if tot == 0:            
        break               # 계산값 0인경우 바로 종료
    elif tot < 0:           # 음수인경우 둘다 음수 or 음수가 큰 경우이므로
        pl += 1             # pl을 우측으로 한칸이동
    else:                   # 양수일 경우 둘다 양수 or 양수가 큰 경우이므로
        pr -= 1             # pr을 좌측으로 
for i in sorted(ans):
    print(i, end=' ')

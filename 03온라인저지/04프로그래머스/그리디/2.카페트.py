import time
start = time.time()  # 시작 시간 저장

import sys

brown,yellow=map(int,sys.stdin.readline().split())
row=col=0
def solution(brown, yellow):
    total=brown+yellow
    for i in range(1,total):
        if total%i==0:
            if (i-2)*(total//i-2)==yellow:
                row,col=i,total//i
                break
    if(row<=col):
        row,col=col,row

    return [row,col]

print(solution(brown,yellow))

print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

    # total=brown+yellow
    # for i in range(1,total):
    #     for j in range((total-1)//i,1,-1):
    #         if (i-2)*(j-2)==yellow and (i*j==yellow+brown):
    #             row,col=i,j
    #             break

import time
import sys
n,m=map(int,sys.stdin.readline().split())
start = time.time()  # 시작 시간 저장
min=10000
data2=[]
for i in range(n):
    data=list(map(int,sys.stdin.readline().split()))
    for j in range(len(data)):
        if min>=data[j]:
            min=data[j]
    data2.append(min)

print(max(data2))


print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
import time
start = time.time()  # 시작 시간 저장

array = [5,9,7,0,3,1,6,2,4,8]

for i in range(len(array)):
    for j in range(i,0,-1):
        if array[j]<array[j-1]:
            array[j],array[j-1]=array[j-1],array[j]
        else : break
print(array)

# 작업 코드
 
 
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
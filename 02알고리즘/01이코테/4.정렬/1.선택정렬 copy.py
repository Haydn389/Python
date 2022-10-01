import time
start = time.time()  # 시작 시간 저장

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i]>array[j]:
            array[i],array[j]=array[j],array[i]

print(array)

# 작업 코드
 
 
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
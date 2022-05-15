import math
import sys


while True:
    n=sys.stdin.readline()
    if n=="\n":break
    n=int(n)
    if n<2:
        print("2이상의 정수를 입력하세요")
        continue
    res=True
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            print("소수가 아닙니다.")
            res=False
            break
    if res==True:
        print("소수입니다.")


# for i in range(2,int(math.sqrt(n))+1):
#     if n%i==0:
#         print("소수가 아닙니다.")
#         res+=1
#         break
# if res==0:
#     print("소수입니다.")



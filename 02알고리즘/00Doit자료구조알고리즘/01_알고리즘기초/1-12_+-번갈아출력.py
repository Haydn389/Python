import sys
print("+와 -를 번갈아 출력합니다.",end=" ")
n=int(sys.stdin.readline())



for i in range(n//2):
    print("+-",end="")

if n%2==1:print("+",end="")


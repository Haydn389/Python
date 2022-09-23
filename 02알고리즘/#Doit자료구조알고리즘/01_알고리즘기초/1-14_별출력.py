import sys
print("*을출력합니다.")
n=int(input("몇 개 출력할까요? : "))
w=int(input("몇 개 마다 줄바꿈 할까요? : "))

#방법1) 
# for i in range(n):
#     print("*",end="")
#     if (i+1)%w==0:print()

#방법2)
for i in range(n//w):
    print("*"*w)
rest=n%w
if rest:
    print("*"*rest)
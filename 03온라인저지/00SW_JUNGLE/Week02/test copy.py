#나눠서 입력받기
# a=list(map(int, input().split()))
# *b,c,d=list(map(int, input().split()))
# print(a)
# print(b)
# print(c)
# print(d)

# #올림
# import math
# print(math.ceil(3.5))

#입력
# 8
# 5 40
# 35 25
# 10 20
# 10 25
# 30 50
# 50 60
# 30 25
# 80 100
n=int(input())
lst = [sorted(list(map(int, input().split()))) for i in range(n)]
print(lst)
# [[5, 40], [25, 35], [10, 20], [10, 25], [30, 50], [50, 60], [25, 30], [80, 100]]

lst.sort(key=lambda x: x[1])
# [[10, 20], [10, 25], [25, 30], [25, 35], [5, 40], [30, 50], [50, 60], [80, 100]]
print(lst)
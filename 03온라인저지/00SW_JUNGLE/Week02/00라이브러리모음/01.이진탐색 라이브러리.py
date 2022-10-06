from bisect import bisect_left, bisect_right, bisect

a = [1, 2, 4, 4,5, 8,8]
x = 4
# print(bisect(a,x))
# print(bisect_left(a, x))
# print(bisect_right(a, x))
# # print(a)

b=[10,20,20,30,40,50]
y=20
print(bisect(b,y))
print(bisect_left(b,y))
print(bisect_right(b,y))

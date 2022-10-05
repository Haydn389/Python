from re import L
import sys
from tkinter import N
input= sys.stdin.readline
n=7
a=[2,1,4,5,1,3,3]
# n=10
# a=[5,10,3,7,12,5,7,2,10,7]
# while True:
#     temp=input().rstrip()
#     num.append(int(temp[0]))
#     data.append(list(map(int,temp[1:].split())))
#     if temp[0] == '0':
#         break
#     i+=1
# print(num)
# print(data)

# while True:
#     a=input().rstrip()
#     n=int(a[0])
#     hi=list(map(int,a[1:].split()))
#     if a[0]=="0":break
area=[None]*n
stack=[]
left=[-1]*n
for i in range(n):#0~n-1
    while stack and stack[-1][1]>=a[i]:
        stack.pop()
    if stack:
        left[i]=stack[-1][0]
    stack.append([i,a[i]])
print(left)

stack=[]
right=[n]*n #오른쪽 넘어선 인덱스
for i in range(n-1,-1,-1): #n-1 ~ 0   n-1-i
    while stack and stack[-1][1]>=a[i]:
        stack.pop()
    if stack:
        right[i]=stack[-1][0]
    stack.append([i,a[i]])
print(right)

area=[(right[i]-left[i]-1)*a[i] for i in range(n)]
print(area)
print(max(area))

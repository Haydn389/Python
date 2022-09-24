#백트래킹 연습1

# pos=[1]*2

# def put():
#     for i in range(2):
#         print(f"{pos[i]}",end=" ")
#     print()

# def set(i):
#     for j in range(1,5):
#         pos[i]=j
#         if i==1:
#             put()
#         else:
#             set(i+1)
# set(0)
# print("="*50)

import sys
n,m=map(int,sys.stdin.readline().split())
# n,m=4,3
#1부터 N까지 자연수 중에서 중복없이 M 개를 고른 (길이가 M인)수열
pos=[0]*m
flag=[False]*(n+1)

def put():
    for i in range(m):
        print(f"{pos[i]}",end=" ")
    print()

def set(i):
    for j in range(1,n+1):
        if not flag[j]:
            pos[i]=j
            if i==(m-1):
                put()
            else:
                flag[j]=True
                set(i+1)
                flag[j]=False  #pos[i]에 j를 넣은 상태에서 set(i+1)에 들어갔다가 모든 과정을 끝났다는 이야기, 즉 
                                #즉 False로 되돌려 다시 사용하고 있지 않음을 명시!
set(0)
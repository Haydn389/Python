# 백트래킹 연습(순열)
# nPm : 서로 다른 n개중에 r개를 선택하는 경우의 수를 의미합니다. (순서 상관 있음)
import sys
n, m = map(int, sys.stdin.readline().split())
# 1부터 N까지 자연수 중에서 중복없이 M 개를 고른 (길이가 M인)수열
# i : 트리의 깊이(N-Queen에서는 열 번호, m과 관련)
# j : 입력되는 값(N-Queen에서는 행 번호, n과 관련)
pos = [0]*m
flag = [False]*(n)
cnt = 0
def put():
    for i in range(m):
        print(f"{pos[i]+1}", end=" ")
    print()

def set(i):
    global cnt
    for j in range(n):
        if not flag[j]:
            pos[i] = j
            if i == m-1:
                # put()
                cnt += 1
            else:
                flag[j] = True
                set(i+1)
                # pos[i]에 j를 넣은 상태에서 set(i+1)에 들어갔다가 모든 과정을 끝났다는 이야기, 즉
                flag[j] = False


                # 즉 False로 되돌려 다시 사용하고 있지 않음을 명시!
set(0)
print(cnt)

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

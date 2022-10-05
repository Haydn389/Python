import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
# n=5
# a=[6,9,5,7,4]
# a=[5,10,13,4,7]

stack = []
ans = [0]*n 

for i in range(n):
    while stack and stack[-1][1] <= a[i]:  # stack의 top이 현재 값보다 크기 전까지 계속 pop()
        stack.pop()
    if stack:   #이후 stakc[-1]이 현재 a[i]탑의 레이저를 수신받는탑임, 
                #만약 stack이 비어있을 경우에는 정답list 업데이트를 건너뛴다
        ans[i] = stack[-1][0] #2차원 배열 중 인덱스만 ans에 저장
    stack.append([i+1, a[i]]) #매번 현재 탑의 index와 value를 저장
print(*ans)

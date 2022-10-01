import sys
n,m=list(map(int,input().split()))
a=[]
for _ in range(n):
    a.append(int(sys.stdin.readline()))
# n, m = 5, 3
# a = [1, 2, 8, 4, 9]  # 1,2,4,8,9
a.sort()
res = 0
# pl = a[1]-a[0]
pl = 1 #가능한 최소거리는 1,2번째 원소의 차이가 아니라 무조건 1임
pr = a[-1]-a[0]

while (pl <= pr):
    mid = (pl+pr)//2
    # mid = 2
    cnt=1 #제일 왼쪽에 무조건 하나 놓고
    value=a[0] #value에 작은 값으로 초기화
    for i in range(1,n):#a길이만큼 반복하면서
        if a[i]-value>=mid:#만약 차이가 mid 이상이면
            cnt+=1          #cnt 추가 후
            value=a[i]      #value 위치를 a[i]로 이동시킴
    if cnt<m:
        pr=mid-1
    else:
        res=mid #내보내야 하는 값은 갯수m이 아니라 거리 임!!
        pl=mid+1

print(res)

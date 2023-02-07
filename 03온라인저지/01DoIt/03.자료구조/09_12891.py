import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=input().rstrip()
p=list(map(int,input().split()))

# print(n,m)
# print(a)
# print(p)

start=0
end=m-1
cnt=0
cur=[0]*4
temp=a[start:end+1]

# cur 초기화
for k in temp:
    if k == 'A':cur[0]+=1
    elif k == 'C':cur[1]+=1
    elif k == 'G':cur[2]+=1
    else :cur[3]+=1

def curAdd(c):
    if c == 'A':cur[0]+=1
    elif c == 'C':cur[1]+=1
    elif c == 'G':cur[2]+=1
    else :cur[3]+=1

def curRemove(c):
    if c == 'A':cur[0]-=1
    elif c == 'C':cur[1]-=1
    elif c == 'G':cur[2]-=1
    else :cur[3]-=1

# 조건 검사함수
def check(cur):
    for j in range(4):
        if p[j] < cur[j]:
            return 0
    return 1

cnt+=check(cur)
start+=1
end+=1

while (end<n):
    # temp=a[start:end+1]
    # print(temp)
    curRemove(a[start-1])
    curAdd(a[end])
    cnt+=check(cur)
    start+=1
    end+=1
print(cnt)
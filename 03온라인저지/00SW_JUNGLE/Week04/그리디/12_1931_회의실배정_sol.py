import sys
input=sys.stdin.readline
n=int(input())
m=[]
for _ in range(n):
    m.append(tuple(map(int,input().split())))
m.sort(key=lambda x:x[1])
res=[m[0]]
for i in range(1,len(m)):
    #이전 회의가 시작시간과 끝 시간이 같고 and 이전 회의시간 끝시간과 다음 회의시간 끝시간이 같다면
    if (res[-1][0]==res[-1][1]) and (res[-1][1]==m[i][1]):
        # cnt+=1
        res.append(m[i])
        continue
    if res[-1][1]<=m[i][0]:
        res.append(m[i])

print(len(res))
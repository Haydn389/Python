import sys

n = sys.stdin.readline().rstrip()
if int(n)<10:
    n="0"+n

res=n
# print(int(n[0])+int(n[1]))
cnt=0
while True:
    res1 = int(res[0])+int(res[1])
    res= res[1]+str(res1)[-1]
    cnt += 1
    if res == n:
        break
    

print(cnt)

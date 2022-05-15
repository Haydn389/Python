import sys

s=sys.stdin.readline().strip()
cnt=[0]*26
s=s.upper()
# print(s)
for i in s:
    cnt[ord(i)-ord('A')]+=1


# print(cnt)
max=max(cnt)
res=[]
for i,a in enumerate(cnt):
    if a==max:
        res.append(i)
# print(res)
if len(res)==1:
    print(chr(res[0]+65))
else: print("?")

# target = input().upper()
# cnt = 0
# ans = ''
# flag = True
# for _ in range(26):
#     temp = target.count(chr(_+65))
#     if temp > cnt:
#         flag = True
#         cnt = temp
#         ans = chr(_+65)
#     elif temp == cnt:
#         flag = False
# if flag == False:
#     print("?")
# else:
#     print(ans)

import sys
input=sys.stdin.readline
s=list(input().rstrip())
key=list(input().rstrip())
a=[[0] *(5) for _ in range(5)]
alpha=['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

left=list(set(alpha)-set(key))
key=list(set(key))
key+=left
for i in range(5):
    for j in range(5):
        a[i][j]=key[i*5+j]
# for x in a:
#     print(x)
# print("------")
# print(s)
res=[]
i=0
while i<len(s)-1:
    if s[i]==s[i+1]:
        if s[i]=='X':
            res.append((s[i],'Q'))
        else:
            res.append((s[i],'X'))
        i-=1
        s.append('X')
    else:
        res.append((s[i],s[i+1]))
    i+=2

# print(res)
def find_idx(c):
    for i in range(5):
        for j in range(5):
            if c==a[i][j]:
                return (i,j)
ans=[]
for c1,c2 in res:
    x1,y1=find_idx(c1)
    x2,y2=find_idx(c2)
    if x1==x2:
        y1=(y1+1)%5
        y2=(y2+1)%5
        ans.append(a[x1][y1]+a[x2][y2])
    elif y1==y2:
        x1=(x1+1)%5
        x2=(x2+1)%5
        ans.append(a[x1][y1]+a[x2][y2])
    else:
        ans.append(a[x1][y2]+a[x2][y1])

# print("***",ans)
print("".join(ans))
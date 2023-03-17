import sys
n,s=map(int,input().split())
a=list(map(int,input().split()))
cnt=0
def func(i,sum):
    global cnt
    if i ==n:
        if sum==s:
            cnt+=1
        return
    func(i+1,sum)
    func(i+1,a[i]+sum)

func(0,0)
if s==0:cnt-=1
print(cnt)
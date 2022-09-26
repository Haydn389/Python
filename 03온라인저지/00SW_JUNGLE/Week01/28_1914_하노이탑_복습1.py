import sys

n=int(sys.stdin.readline())
cnt=0
def h(n,a,b,c):
    global cnt
    if n==1:
        print(a,b)
        cnt+=1
    else:
        h(n-1,a,b,c)
        print(a,c)
        cnt+=1
        h(n-1,b,c,a)

if n<=20:
    h(n,1,3,2)
    print(cnt)

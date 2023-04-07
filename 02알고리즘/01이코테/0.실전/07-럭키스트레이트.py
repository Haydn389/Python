import sys
input = sys.stdin.readline

a=input().rstrip()

n=len(a)//2
r=a[:n]
l=a[n:]
r_sum=l_sum=0
for i in range(n):
    r_sum+=int(r[i])
    l_sum+=int(l[i])

if r_sum == l_sum:
    print("LUCKY")
else:
    print("READY")
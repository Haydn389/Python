import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a=input().split()
    num=int(a[0])
    res=''
    for c in a[1]:
        res+=c*num
    print(res)
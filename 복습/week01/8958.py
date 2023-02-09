import sys
input = sys.stdin.readline

for _ in range(int(input())):
    sum=0
    a=input().split('X')
    print(a)
    for x in a:
        if 'O' in x:
            n=len(x)
            sum+=n*(n+1)/2
    print(int(sum))



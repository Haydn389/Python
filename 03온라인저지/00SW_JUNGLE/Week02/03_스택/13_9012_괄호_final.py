import sys
input=sys.stdin.readline
n=int(input())

for _ in range(n):
    a=input().rstrip()
    s=[]
    flag=True
    for p in a:
        if p==")":
            if len(s)==0:
                flag=False
                print("NO")
                break
            else:s.pop()
        else:
            s.append("(")
    if flag:
        if len(s)!=0:
            print("NO")
        else:
            print("YES")
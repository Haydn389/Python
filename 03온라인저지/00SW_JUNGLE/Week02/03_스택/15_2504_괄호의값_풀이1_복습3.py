import sys
input=sys.stdin.readline
s=sys.stdin.readline().rstrip()

temp=1
res=0
stack=[]

for i in range(len(s)):
    if s[i]=="(":
        temp*=2
        stack.append(s[i])
    elif s[i]=="[":
        temp*=3
        stack.append(s[i])
    elif s[i]==")":
        if len(stack)==0 or stack[-1]=="[":
            res=0
            break
        if s[i-1]=="(":
            res+=temp
        stack.pop()
        temp//=2
    else:
        if len(stack)==0 or stack[-1]=="(":
            res=0
            break
        if s[i-1]=="[":
            res+=temp
        stack.pop()
        temp//=3
if len(stack)!=0:
    res=0

print(res)
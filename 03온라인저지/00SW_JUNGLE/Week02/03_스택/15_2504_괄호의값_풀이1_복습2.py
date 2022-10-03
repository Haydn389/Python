import sys

s=sys.stdin.readline().strip()

temp=1
res=0
stack=[]
for i in range(len(s)):
    if s[i]=="(":
        stack.append(s[i])
        temp*=2
    elif s[i]=="[":
        stack.append(s[i])
        temp*=3
    elif s[i]==")":
        if len(stack)==0 or stack[-1]=="[":
            res=0
            break
        if s[i-1]=="(":
            res+=temp
        temp//=2
        stack.pop()
    else: #s[i]=="]"
        if len(stack)==0 or stack[-1]=="(":
            res=0
            break
        if s[i-1]=="[":
            res+=temp
        temp//=3
        stack.pop()
if len(stack)!=0 :
    res=0
print(res)
import sys
s=input()
stack=[]
cnt=0
for i in range(len(s)):
    if s[i]=="(":
        stack.append(s[i])
    else: #")"
        if stack[-1]=="(":
            stack.pop()
            cnt+=len(stack)
        else:
            stack.pop()
            cnt+=1
print(cnt)
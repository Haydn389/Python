s=input()
stack=[]
cnt=0
for i in range(len(s)):
    if len(stack)==0:
        if s[i]=="(":
            stack.append(s[i])
        else: #s[i]==")"
            cnt+=1
    else:
        if s[i]=="(":
            stack.append(s[i])
        else:
            stack.pop()

print(cnt+len(stack))
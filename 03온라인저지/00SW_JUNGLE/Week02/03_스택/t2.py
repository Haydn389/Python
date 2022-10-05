import sys

a=input().rstrip()
stack=[]
res=0
for i in range(len(a)):
    if a[i] =="(":
        stack.append("(")
    elif a[i]==")":
        if a[i-1]=="(":
        # if stack and stack[-1]=="(":
            stack.pop()
            res+=len(stack)
        else:
            stack.pop()
            res+=1
print(res)

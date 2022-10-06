s = input()
stack = []
cnt = 0
for i in range(len(s)):
    if s[i] == "(":
        stack.append(s[i])
    elif not stack:
        cnt += 1
    else:
        stack.pop()
        
print(cnt+len(stack))

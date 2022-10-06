import sys
input=sys.stdin.readline
s=input().rstrip()
c=input().rstrip()

# print(s)
# print(c)
half=len(c)//2

if len(c)%2==0:
    front=c[:half]
    mid=[]
    end=c[half:]
else:
    front=c[:half]
    mid=c[half]
    end=c[half+1:]
# end=c[half:]
# print(front)
# print(end)
stack=[]
for i in range(len(s)):
    t_front=front
    t_mid=mid
    t_end=end
    if s[i] in front:
        stack.append(s[i])
    elif s[i] in mid:
        if stack[-1] in front:
            continue
        else:stack.append(s[i])
    elif s[i] in end:
        if stack[-1] in front:
            stack.pop()
        else:stack.append(s[i])
    else:
        stack.append(s[i])
if stack:
    print("".join(stack))
else:
    print("FRULA")
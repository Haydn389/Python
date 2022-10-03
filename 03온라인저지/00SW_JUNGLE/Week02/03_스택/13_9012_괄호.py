import sys
n = int(sys.stdin.readline())


for i in range(n):
    stack=[]
    cmd=sys.stdin.readline().rstrip()
    flag=True
    for p in cmd:
        if p=='(':
            stack.append(1)
            # print(">>>",stack)
        else:
            try:
                stack.pop()
                # print(">>>",stack)
            except IndexError:
                flag=False
                print("NO")
                break
    if flag:
        if len(stack)==0:
            print("YES")
        else:print("NO")
            
# print(sum(stack))
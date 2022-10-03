import sys
# a = sys.stdin.readline().rstrip()
a = "(()[[]])([])"
# a = "[][]((])"
st = []
temp = 0
ans = 0
for i in range(len(a)):
    temp=0
    if a[i] == "(":
        st.append("(")
    elif a[i] == "[":
        st.append("[")
    else:  # )or]
        top=a.pop()
        if a[-1] == ")":
            if a[i-1] == "(":
                st.pop()
                temp += 2
            elif a[i-1] == "[":
                break
            else:
                temp *= 2
        else:  # "]"
            if a[i-1] == "[":
                st.pop()
                temp += 3
            elif a[i-1] == "(":
                break
            else:
                temp *= 3
    ans+=temp
print(ans)

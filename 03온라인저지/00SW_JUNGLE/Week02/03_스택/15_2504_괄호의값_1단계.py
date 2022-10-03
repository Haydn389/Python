import sys
# a = sys.stdin.readline().rstrip()
a = "(()[[]])([])"
a = "(((()())))"
st=[]
temp=0
cnt=0
for i in range(len(a)):
    if a[i] in "(":
        st.append("(")
            
    else:
        if a[i-1]=="(":
            st.pop()
            temp+=2
        else:
            st.pop()
            temp*=2
print(temp)
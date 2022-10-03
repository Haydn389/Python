import sys
a = sys.stdin.readline().rstrip()
st=[]
cnt=0
for i in range(len(a)):
    if a[i]=="(":
        st.append("(")

    else:
        if a[i-1]=="(":
            st.pop()
            cnt+=len(st)
        else:
            st.pop()
            cnt+=1
print(cnt)
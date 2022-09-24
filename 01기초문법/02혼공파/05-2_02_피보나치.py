# f(1)=1,f(2)=1
# f(n)=f(n-1)+f(n-2)


def f(n):
    global cnt
    cnt +=1
    if n <=2:
        return 1
    else:
        return f(n-1)+f(n-2)
cnt=0
print(f(35))
print(cnt)

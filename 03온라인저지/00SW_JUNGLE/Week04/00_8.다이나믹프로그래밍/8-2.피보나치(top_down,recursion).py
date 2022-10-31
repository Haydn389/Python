d=[0] *11

def fibo(x):
    print('f('+str(x)+')',end=" ")
    if x==1 or x==2:
        return 1
    if d[x]!=0:
        return d[x]
    d[x]=fibo(x-1)+fibo(x-2)
    return d[x]
#주석의 색은
print(fibo(10))

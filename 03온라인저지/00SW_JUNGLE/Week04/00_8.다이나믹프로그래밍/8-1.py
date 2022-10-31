def fibo(x):
    global cnt
    if x==1 or x==2:
        print(cnt)
        cnt+=1
        return 1
    return fibo(x-1) + fibo(x-2)

cnt=1
print((fibo(10)))
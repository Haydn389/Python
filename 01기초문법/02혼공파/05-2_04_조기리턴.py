memo={
    1:1,
    2:1
}

def f(n):
    if n in memo:
        return memo[n]
    else:
        output=f(n-1)+f(n-2)
        memo[n]=output
        return output
print(f(5))
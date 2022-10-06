import sys
sys.setrecursionlimit(10**8)
n = int(sys.stdin.readline())
res = ""
sum = 0
ans=""
def moo(n):
    global res, sum
    # sum += len(res)
    if sum>n:
        res+=""
        return
    elif n == 0:
        res += "moo"
        sum+=len(res)
        return
    else:
        # if sum>n:return
        # sum += len(res)
        moo(n-1)
        res +="m"+"o"*(n+2)
        moo(n-1)
        sum+=len(res)
        return

moo(n)
print(res)
# print(res[n-1])

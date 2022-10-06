import sys
sys.setrecursionlimit(10**8)  # 10^8 까지 늘림
n = int(sys.stdin.readline())
res = ""
sum = 0

def moo(n):
    global res, sum
    sum += len(res)
    # print("길이합",sum)
    # if len(res) > n:
    #     return
    if n == 0:
        res = "moo"
        return res
    else:

        res = res+moo(n-1)+"m"+"o"*(n+2)+moo(n-1)
        # print(len(res))
        print("길이합", sum)
        # if sum > n:
            # break
        # if sum > n:
        #     break
        return res


moo(n)
print(res[n-1])

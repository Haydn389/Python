n = int(input())
cnt = 0


def h(n, s, e, m):  # 갯수, 시작, 목표, 보조
    global cnt, flag
    cnt += 1
    if n == 1:
        if flag:
            print(s, e)
        return
    else:
        h(n-1, s, m, e)
        if flag:
            print(s, e)
        h(n-1, m, e, s)


flag = False
if n <= 20:
    flag = True
h(n, 1, 3, 2)
print(cnt)

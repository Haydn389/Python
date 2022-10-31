import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
plug = []
for i in range(len(a)):
    if a[i] in plug:
        continue
    elif len(plug) < n:
        plug.append(a[i])
        continue
    idx = []
    idx_first = []
    flag = False
    for p in plug:
        try:
            idx.append([a[i+1:].index(p), p])
        except:
            idx_first.append(plug.index(p))
            plug[plug.index(p)] = a[i]
            cnt += 1
            flag = True
            break
    if flag:
        continue
    else:
        idx.sort(reverse=True)
        plug[plug.index(idx[0][1])] = a[i]
        cnt += 1
print(cnt)

import sys
input=sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))

cnt=0
plug=[]
for i in range(len(a)):
    if a[i] in plug:
        continue
    elif len(plug)<n:
        plug.append(a[i])
        continue
    idx=[]
    idx_first=None
    for p in plug:
        try:
           idx.append([a[i+1:].index(p),p])
        except:
            idx_first=plug.index(p)
            break
    if idx_first!=None:
        plug[idx_first]=a[i]
        cnt+=1
    else:
        idx.sort(reverse=True)
        plug[plug.index(idx[0][1])]=a[i]
        cnt+=1

    
print(cnt)
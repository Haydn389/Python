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
    idx_first=[]
    for p in plug:
        try:
           idx.append(a[i+1:].index(p))
        except:
            idx_first.append(plug.index(p))
            break
    if idx_first:
        plug[idx_first[0]]=a[i]
        cnt+=1
        continue
    if idx:
        plug[plug.index(a[i+1:][max(idx)])]=a[i]
        cnt+=1

    
print(cnt)
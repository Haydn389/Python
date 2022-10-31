import sys
input=sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))


# use=[*a[:n]]
first=list(set(a[:n]))
use=[0]*n
for i in range(len(first)):
    use[i]=first[i]
cnt=0
# print(use)
for i,num in enumerate(a[n:]):
    # print(">>",use)
    # print(num,a[(i+n)+1:(i+n)+n+1])
    if num in use:
        continue
    if 0 in use:
        zero_idx=use.index(0)
        use[zero_idx]=num
        # cnt+=1
        continue
    flag=True
    for u in use:
        # if u not in a[(i+n)+1:(i+n)+n]:
        # if u not in a[(i+n)+1:] or u==a[-1]:
        if u not in a[(i+n)+1:]:
            idx=use.index(u)
            use[idx]=num
            cnt+=1
            flag=False
            break
    if flag:
        m_idx=0
        for u in use:
            m_idx=max(m_idx,a[(i+n)+1:].index(u))
        use[m_idx]=num
        cnt+=1
    
print(">>",use)

print(cnt)
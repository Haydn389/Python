a=[9,1,3,4,6,7,8]
cnt=0
def b(a):
    global cnt
    right=len(a)-1
    left=0
    last=None
    
    while(left<right):
        for j in range(right,left,-1):
            cnt+=1
            if a[j-1]>a[j]:
                a[j-1],a[j]=a[j],a[j-1]
                last=j
        left=last
        for j in range(left,right):
            cnt+=1
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                last=j
        right=last

b(a)
print(a)
print(cnt)


#1.버블정렬

a=[9,7,5,1,4,6,8]
aa=[9,1,3,4,6,7,8]
b=[9,7,5,1,4,6,8]
c=[9,7,5,1,4,6,8]
cnt_a=0
cnt_aa=0
cnt_b=0
cnt_c=0

def bubble_sort(a):
    global cnt_a
    n=len(a)
    for i in range(n):
        for j in range(n-1,i,-1):
            if a[j-1]>a[j]:
                a[j-1],a[j]=a[j],a[j-1]

def shaker_sort(aa):
    global cnt_aa
    n=len(a)
    right=n-1
    left=0
    last=right
    while(left<right):
        for i in range(right,left,-1):
            if aa[i-1]>aa[i]:
                aa[i-1],aa[i]=aa[i],aa[i-1]
                last=i   
                cnt_aa+=1
        left=last
        
        for i in range(left,right):
            if aa[i]>aa[i+1]: ###틀린부분
                aa[i],aa[i+1]=aa[i+1],aa[i]
                cnt_aa+=1
                last=i   
        right=last

def select_sort(b):
    global cnt_b
    n=len(b)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if b[min]>b[j]:
                min=j
        b[i],b[min]=b[min],b[i]

        cnt_b+=1
        print(*b)
        

def insert_sort(c):
    global cnt_c
    n=len(c)
    for i in range(n):
        temp=c[i]
        j=i
        while j>0 and c[j-1]>temp: #if문 안에 또 없어도됨
            c[j]=c[j-1]                                                     
            j-=1
        c[j]=temp
        cnt_c+=1
        
        print(*c)

# bubble_sort(a)
# print("버블:{:<3} {}".format(cnt_a,a))

shaker_sort(aa)
print("셰이커:{:<3} {}".format(cnt_aa,aa))

# select_sort(b)
# print("선택:{:<3} {}".format(cnt_b,b))

# insert_sort(c)
# print("삽입",cnt_c,c)


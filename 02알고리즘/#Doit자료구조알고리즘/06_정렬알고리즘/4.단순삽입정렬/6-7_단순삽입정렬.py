# a=[1,4,6,7,3,9,8]
a=[6,4,1,7,3,9,8]
a=[9,4,1,7,6,8,3,5,2]
cnt=0
def straight_insertion_sort(a):
    global cnt
    n=len(a)
    for i in range(1,n):#i=1~6
        temp=a[i]
        j=i
        while j>0 and a[j-1]>temp: #temp보다 왼쪽값이 크다면
            a[j]=a[j-1] #a[j]위치에 덮어쓰기!
            j-=1
            cnt+=1
        a[j]=temp #마지막으로 덮어쓴 j 왼쪽값(j-=1)에 최종적으로 temp 덮어쓰기
straight_insertion_sort(a)
print(a)
print(cnt)
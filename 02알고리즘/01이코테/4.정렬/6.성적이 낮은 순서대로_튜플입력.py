import sys

n=int(sys.stdin.readline().strip())
array=[]

for i in range(n):
    # data=input().split()
    data=sys.stdin.readline().split()
    # array+=[(data[0],int(data[1]))]
    array.append((data[0],data[1]))
array=sorted(array,key=lambda i : i[1])

for i in array:
    print(i[0],end=' ')
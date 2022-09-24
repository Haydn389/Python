x,y=map(int,input().split())
t=int(input())
x=["1"]*x
y=["1"]*y
x_slice=[]
x_slice=[]

for _ in range(t):
    a,b=map(int,input().split())
    if a==0:
        y.insert(b,"#")
    else:
        x.insert(b,"#")

print(x,y)
y_slice="".join(y)
x_slice="".join(x)
print(x,y)
x=list(map(len,x_slice.split("#")))
y=list(map(len,y_slice.split("#")))
print(x,y)
print(max(x)*max(y))


# a="0123456789"

# print(a[3:5])
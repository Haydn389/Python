x, y = map(int, input().split())
t = int(input())

x = [0, x]
y = [0, y]

for i in range(t):
    a, b = map(int, input().split())
    if a == 0:
        y.append(b)
    else:
        x.append(b)

# print(sorted(x),sorted(y))

x=sorted(x)
y=sorted(y)

# print(type(x),type(y))
sub_x=[]
sub_y=[]

for i in range(1,len(x)):
    sub_x.append(x[i]-x[i-1])
for i in range(1,len(y)):
    sub_y.append(y[i]-y[i-1])

# print(sub_x)
# print(sub_y)

print(max(sub_x)*max(sub_y))
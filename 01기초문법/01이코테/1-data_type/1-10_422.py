array=[i for i in range(20)if i%2==1]
print(array)

array=[]
for i in range(20):
    if i%2==1:
        array.append(i)
print(array)

array=[i*i for i in range(1,10)]
print(array)

c=[1,3,5,4,8,5,7,8,6,5,4,2,74,8,2]
array=[i for i in c if i%2==1]
print(array)

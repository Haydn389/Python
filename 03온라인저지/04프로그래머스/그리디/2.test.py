# a = ['hong','gil','dong']
# b = []

# for i,name in enumerate(a):
#     b.append((i,name))

# print(b)

#01
test = [1,2,3]
for index, value in enumerate(test): 
    print(index,value)

#02 
a = ['name','python', 'type','snake']
c = {} 
for i,name in enumerate(a):
    c[i] = a[i]
print(c)

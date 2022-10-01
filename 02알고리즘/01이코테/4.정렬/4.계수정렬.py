array=[5,4,5,7,8,9,2,4,4,8,0,1,3,5,6,7]

count=[0]*(max(array)+1)

for i in range(len(array)):
    count[array[i]]+=1
print(count)


# for i in range(len(count)):
#     for j in range(count[i]):
#         print(i,end=" ")
data=[[1]*10 for _ in range(10)]


print(*data, sep=" ")
for i in range(len(data)):
    for j in range(len(data)):
        print(data[i][j],end=" ")
    print()    

lst = ['x','y','z']
print(*lst, sep = ' ')

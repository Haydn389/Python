n=int(input())

array=[]
for i in range(n):
    array.append(list(map(int,input().split())))

print(array)

for i in range(n):
    print(f"#{i+1} {int(round(sum(array[i])/10,0))}")
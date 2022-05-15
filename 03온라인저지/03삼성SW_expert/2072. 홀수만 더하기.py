import sys

n=int(sys.stdin.readline().strip())
data=[]
for _ in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    data[i]=[ c for c in data[i] if c %2!=0]
    print("#"+str(i+1),sum(data[i]))

# print(data)
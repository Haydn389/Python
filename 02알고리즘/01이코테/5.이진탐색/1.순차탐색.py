import sys

data = sys.stdin.readline().split() #str
n=int(data[0])
target=data[1]

array = sys.stdin.readline().split() #str
check=False
for i in range(len(array)):
    if target==array[i]:
        print(i+1)
        check=True
        break
if check==False:
    print("찾는 문자가 없습니다.")
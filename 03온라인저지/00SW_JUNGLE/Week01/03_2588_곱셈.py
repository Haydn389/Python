first_num=int(input())
second_num=input()

for i in range(2,-1,-1):
    res=first_num*int(second_num[i])
    print(res)
print(first_num*int(second_num))

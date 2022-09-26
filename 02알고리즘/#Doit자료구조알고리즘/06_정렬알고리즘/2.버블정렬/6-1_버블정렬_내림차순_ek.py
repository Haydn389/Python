data=[6,4,3,7,1,9,8]
n=len(data)
ans=[None]*n
for i in range(n): # *n이 아니라 n-1이어야함
    for j in range(n-i-1):
    # for j in range(n-1): #비효율적인 코드 
        # print("i={},j={}".format(i,j))
        # print(data[j],end="|" )
        # print(data[j+1])
        if data[j]<data[j+1]:
            data[j],data[j+1]=data[j+1],data[j]
    # print("---------------------")
# print()

print(data)
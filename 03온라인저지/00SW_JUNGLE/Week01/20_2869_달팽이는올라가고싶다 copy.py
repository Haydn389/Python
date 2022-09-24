import math
a,b,v=map(int,input().split())

# print(a,b,v)
k=(v-a)/(a-b)
print(math.ceil(k)+1)


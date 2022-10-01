import math
a,b,v=map(int,input().split())

k=(v-a)/(a-b)

print(math.ceil(k)+1)
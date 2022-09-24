#https://youtu.be/FiR7NmEE8AY
import math
import sys
a,b,v=map(int,sys.stdin.readline().split())

##풀이1
k=(v-a)//(a-b)
if (v-a)%(a-b)==0:
    print(k+1)
else:
    print(k+2)

##풀이2
# k(v-a)/(a-b)
# print(math.ceil(k)+1)


##풀이3
# A, B, V = map(int, input().split())
# day = (V - B) / (A - B)
# print(math.ceil(day))
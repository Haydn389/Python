import math
import sys
a,b = map(int,sys.stdin.readline().split())

def lcm(a,b):
    return a*b//math.gcd(a,b)

print(math.factorial(a))
print(math.sqrt(a))
print(math.gcd(a,b))
print(lcm(a,b))
print(math.pi)
print(math.e)


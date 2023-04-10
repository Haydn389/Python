from itertools import permutations #순열
from itertools import combinations #조합
from itertools import product #중복순열
from itertools import combinations_with_replacement #중복조합
import sys
data=[10,20,30]

print("순열"+"*"*50)
print(list(permutations(data,2))) #뒤에 안적으면 n!이랑 같음

print("조합"+"*"*50)
print(list(combinations(data,2)))

print("중복순열"+"*"*50)
print(list(product(data,repeat=2))) #reqpeat을 적어줘야함

print("중복조합"+"*"*50)
print(list(combinations_with_replacement(data,2)))

# print("*"*50)
# test=["1","1","2","3","4"]
# print(list(permutations(test,5)))
# print(len(list(permutations(test,5))))

# print(set(permutations(test,5)))
# print(len(set(permutations(test,5))))

print("*"*50)
#input에서 입력받는 내용은 항상 문자열임 
a=input('첫 번째 숫자를 입력하세요 : ')
b=input('두 번째 숫자를 입력하세요 : ')
print(type(a))

def add(x,y):
    return x+y
print(add(a,b))

# https://youtu.be/uIcK7-YU8uA?list=PLBvj5lBPsUDeO5MIiwrV7Ei6pW2fa3uRo
#1)클래스 생성하기
class JSS:
    #init 함수를 
    #self 클래스 자신을 저장할 변수
    def __init__(self) -> None: 
        # print("JSS클래스 선언!")
        self.name=input("이름:")
        self.age=input("나이:")
    def show(self):
        print("나의 이름은 {}. 나이는 {}세입니다.".format(self.name,self.age))
# a=JSS()
#위에서 클래스 선언시 사용한 self는 a를 뜻함
#self가 a로 대치된다고 이해하자
# print(a.name)
# print(a.age)
# a.show()

#2)상속하기
class JSS2(JSS): #괄호안에 상속받을 클래스를 넣는다. 
    def __init__(self): #기존 내용을 버리고 덮어씀
        super().__init__() #상속받는 클래스의 init함수를 들고올수있므
        self.gender = input("성별:")
    def show(self):
        print("나의 이름은 {}.성별{}, 나이는 {}세입니다.".format(self.name,self.age,self.age))

a=JSS2()
a.show()
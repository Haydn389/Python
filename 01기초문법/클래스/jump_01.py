from unittest import result


class FourCal:
    def __init__(self,first,second): #메서드의 매개변수
        self.first=first            #메서드의 수행문
        self.second=second          #메서드의 수행문
    def add(self):
        result=self.first + self.second
        return result
    def div(self):
        result=self.first /self.second
        return result
# 1) 객체a의 생성
a=FourCal(4,2)
b=FourCal(3,7)
# print(type(a)) #객체 a가 어떤 타입인지 알아보자 : FourCal 클래스의 인스턴스임을 알 수있다.

# 2) 객체에 숫자 지정할 수 있게 만들기
# a.setdata(4,2) #생성자를 만들면 필요없음
print(a.first)
print(a.second)
# b.setdata(3,7)
print(b.first)
print(b.second)

print(a.add())

class MoreFourCal(FourCal):
    def pow(self):
        result=self.first**self.second
        return result

class SafeFourCal(FourCal):
    def div(self):
        if self.second==0:
            return 0
        else:
            return self.first/self.second

c=MoreFourCal(3,0)
print(c.add())
print(c.pow())
# print(c.div()) #zerodiv 오류발생

d=SafeFourCal(3,0) #새 클래스에 기존 클래스 상속한 후 메서드오버라이딩 하여 해결
print(d.div()) #zerodiv 오류발생 안함
print("----")
d.a=SafeFourCal(3,0)
print(d.a.div())
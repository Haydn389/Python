class Node:
    def __init__(self,item,next):
        self.item=item
        self.next=next
class Stack:
    def __init__(self):
        self.top=None

    def push(self,item):
        self.top=Node(item,self.top)#기존의 None을 새로 추가하는 값의 next로 설정
    
    def pop(self):
        item=self.top.item
        self.top=self.top.next
        return item
    def isEmpty(self):
        return not self.top

s1=Stack()
print(s1.isEmpty())
s1.push(1)
s1.push(2)
print(s1.isEmpty())
s1.pop()
s1.pop()
print(s1.isEmpty())


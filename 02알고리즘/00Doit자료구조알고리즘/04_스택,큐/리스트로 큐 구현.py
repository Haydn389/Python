class Node:#클래스 이름
    def __init__(self,item,next):#매개변수
        self.item=item #해당 메서드의 속성 = 매개변수
        self.next=next

class Stack:
    def __init__(self):
        self.last=None
    
    def push(self,item):
        self.last=Node(item,self.last)#새로 추가된 노드가 기존의 last를 가리키고, last가 새로추가된 노드를 가리키도록 설정
    def pop(self):
        item=self.last.item #last의 값을 반환 
        self.last = self.last.next #last를 last의 다음 값으로 설정
        return item
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)


for _ in range(5):
    print(stack.pop())
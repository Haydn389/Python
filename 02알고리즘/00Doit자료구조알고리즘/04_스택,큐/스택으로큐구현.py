class myQueue:
    def __init__(self):
        self.input=[]
        self.output=[]

    def push(self,item):
        self.input.append(item)

    def pop(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output.pop()
    
    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

q=myQueue()

q.push(1)
q.push(2)
q.push(3)
q.push(4)
print(q.input, q.output)
print(q.pop())
q.push(5)
q.push(6)
print(q.input, q.output)
print(q.pop())
print(q.input, q.output)
print(q.pop())
print(q.input, q.output)
print(q.pop())
print(q.input, q.output)
q.push(7)
print(q.input, q.output)
print(q.pop())
print(q.input, q.output)
print(q.pop())
print(q.input, q.output)
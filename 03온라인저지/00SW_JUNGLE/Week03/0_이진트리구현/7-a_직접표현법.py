class Node:
    # def __init__(self,key):
    #     self.key=key
    #     #처음에는 None으로 초기화
    #     self.parent=self.left=self.right=None
    def __init__(self,key,parent=None,left=None,right=None):
        self.key=key
        #처음에는 None으로 초기화, 위 방법도 가능
        self.parent=parent
        self.left=left
        self.right=right

    def __str__(self):
        return str(self.key)

a=Node(6)
b=Node(9)
c=Node(1)
d=Node(5)

a.left=b
b.right=c
b.parent=c.parent=a
b.right=d
d.parent=b
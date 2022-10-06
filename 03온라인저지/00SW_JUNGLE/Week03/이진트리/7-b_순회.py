class Node:
    # def __init__(self,key):
    #     self.key=key
    #     #처음에는 None으로 초기화
    #     self.parent=self.left=self.right=None
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        # 처음에는 None으로 초기화, 위 방법도 가능
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.key)

    def preorder(self):  # 현재 방문중인 노드=self
        if self != None:
            print(self.key) #1)현재 노드 방문
            if self.left:  # 현잰 방문중인 노드에 왼쪽노드가 있다면
                self.left.preorder()
            if self.right:  # 현잰 방문중인 노드에 오른쪽 노드가 있다면
                self.right.preorder()

    def inorder(self):  # 현재 방문중인 노드=self
        if self != None:
            if self.left:  # 현잰 방문중인 노드에 왼쪽노드가 있다면
                self.left.inorder()
            print(self.key)
            if self.right:  # 현잰 방문중인 노드에 오른쪽 노드가 있다면
                self.right.inorder()

    def postorder(self):  # 현재 방문중인 노드=self
        if self != None:
            if self.left:  # 현잰 방문중인 노드에 왼쪽노드가 있다면
                self.left.postorder()
            if self.right:  # 현잰 방문중인 노드에 오른쪽 노드가 있다면
                self.right.postorder()
            print(self.key)


a = Node(6)
b = Node(9)
c = Node(1)
d = Node(5)

a.left = b
b.right = c
b.parent = c.parent = a
b.right = d
d.parent = b

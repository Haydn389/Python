import sys
sys.setrecursionlimit(1000)
input= sys.stdin.readline

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.root = None

    def add(self, data): #새로 받은 값
        if (self.root == None): #트리가 비어있다면
            self.root =Node(data)
        else: #트리가 비어있지 않다면
            cur= self.root #현재 노드를 루트노드 초기화
            while (True):
                if (cur.data>data): #현재노드와 입력값 비교 => 작을때
                    if (cur.left==None):  #왼쪽자식 비어있으면
                        cur.left=Node(data) #왼쪽자식으로 지정 후 break
                        break
                    cur=cur.left #아니면 왼쪽노드로 이동 후 반복
                else:
                    if (cur.right==None):
                        cur.right=Node(data)
                        break
                    cur=cur.right

    def post_order(self,node):
        if node == None:
            node = self.root
        if node.left != None:
            self.post_order(node.left)
        if node.right != None:
            self.post_order(node.right)
        print(node.data)

tree = Tree()
while True:
    try:
        tree.add(int(input()))
    except:
        break
print("=============")
tree.post_order(None)
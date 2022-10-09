from multiprocessing.connection import answer_challenge
import sys
sys.setrecursionlimit(20000)
input = sys.stdin.readline

class Node:
    def __init__(self,key) -> None:
        self.key=key
        self.left=None
        self.right=None

class BST:
    def __init(self):
        self.root=None

    def add(self,key):         
        if self.root==None:     #루트노드가 None이면 즉 빈 트리이면
            self.root=Node(key)    #현재 값을 루트노드로 추가

        else:
            current=self.root
            while True:
                if current.key>key:
                    if current.left==None:
                        current.left=Node(key)
                        break
                    current=current.left
                if current.key<key:
                    if current.right==None:
                        current.left=Node(key)
                        break
                    current=current.right
                    
    def postOrder(self,node=None):
        if node==None:
            node=self.root
        if node.left!=None:
            self.postOrder(node.left)
        if node.right!=None:
            self.postOrder(node.right)
        answer.append(node.data)



tree=BST()

while True:
    try:
        tree.add(int(input()))

    except:
        break
answer=[]

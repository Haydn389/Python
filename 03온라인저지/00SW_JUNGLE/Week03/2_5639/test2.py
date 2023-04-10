import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.root=None
    def add(self,data):
        if self.root==None:
            self.root=Node(data)
        else:
            cur=self.root
            while(True):
                if cur.data < data:
                    if cur.right ==None:
                        cur.right=Node(data)
                        break
                    cur=cur.right
                else:
                    if cur.left ==None:
                        cur.left=Node(data)
                        break
                    cur=cur.left

    def post_order(self,node):
        if node == None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.data)

tree=Tree()

while(True):
    try:
        tree.add(int(input()))
    except:
        break

tree.post_order(tree.root)

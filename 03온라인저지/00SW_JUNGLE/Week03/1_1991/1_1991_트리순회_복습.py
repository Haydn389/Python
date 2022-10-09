class Node:
    def __init__(self,key,left,right) -> None:
        self.key=key
        self.left=left
        self.right=right

def pre_order(self):
    print(self.key,end="")
    if self.left!=".":
        pre_order(tree[self.left])
    if self.right!=".":
        pre_order(tree[self.right])

def in_order(self):
    if self.left!=".":
        in_order(tree[self.left])
    print(self.key,end="")
    if self.right!=".":
        in_order(tree[self.right])

def post_order(self):
    if self.left!=".":
        post_order(tree[self.left])
    if self.right!=".":
        post_order(tree[self.right])
    print(self.key,end="")




n=int(input())
tree={}
for _ in range(n):
    key,left,right=input().split()
    tree[key]=Node(key,left,right)

pre_order(tree["A"])
print()
in_order(tree["A"])
print()
post_order(tree["A"])
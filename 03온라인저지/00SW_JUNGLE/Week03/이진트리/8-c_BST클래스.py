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
class BST:
    #생성자 : 
    # 비어있기 때문에 root는 아무것도 가리키지 않고
    # 비어있기 때문에 size는 0
    def __init__(self):
        self.root=None
        self.size=0

    #여러개의 node가 insert 혹은 delete될텐데
    #현재 node 수를 반환하는 메서드
    def __len__(self):
        return self.size

    # class 내의 __iter__() method를 호출
    # 예) root노드부터 시작하여 pre/in/post order로 방문하라는 뜻
    def __iter__(self):
        return self.root.__iter__()

    def find_loc(self,key):
        if self.size==0: #빈 트리다, 처음으로 들어가려 하는데 트리자체가 비어있음 
                        #--> 부모노드를 return 해야하는데 root노드의 부모노드는 없으니 None을 return
            return None
        p=None #p는 v의 부모
        v=self.root # 
        while v:
            if v.key==key:return v #key가 일치하면 해당 노드를 return
            elif v.key<key:
                p=v
                v=v.right
            else:
                p=v
                v=v.left
        return p #leafnode까지 갔는데 key가 없다면 삽입될 위치의 부모노드를 return
    
    def search(self,key):
        v=self.find_loc(key)
        if v==None:
            return None
        else: return v
    def insert(self,key):
        p=self.find_loc(key)
        if p==None or p.key!=key:
            v=Node(key)
            if p==None:
                self.root=v
            else:
                v.parent=p
                if p.key>=key:
                    p.left=v
                else:
                    p.right=v
        else:
            print("key is already in the tree!")
            return p

    
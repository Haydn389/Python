from __future__ import annotations
from typing import Any, Type


class Node:
    def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None  # root에 None을 대입하여 노드가 하나도 없는 빈상태의 이진검색트리 생성

    def search(self, key: Any) -> Any:
        p = self.root
        while True:
            if p is None:       #만약 빈 트리여서 처음에 self.root 가 None이거나 탐색을 지속하던 중 leaf노드를 만나 자식노드가 없으면 수행
                return None
            if key == p.key:
                return p.value
            elif key < p.key:
                p = p.left
            else:
                p = p.right

    def add(self, key: Any, value: Any) -> bool:
        # 키가 key이고 값이 value인 노드를 삽입
        def add_node(node: Node, key: Any, value: Any) -> None:
            # 매번 호출되면서 새로 전달 된 node를 루트로 하는 서브트리에 키가 key이고 값이 value인 노드 삽입
            if key == node.key:
                return False  # 이미 같은 key가 존재
            elif key < node.key:
                if node.left is None:
                    # 새로 삽입하는 노드는 리프노드가 됨
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            return True  # 새 key를 정상적으로 삽입 후 종료

        if self.root is None:  # root노드가 없으면 루트노드에 삽입 후 바로종료
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)

    def remove(self,key:Any)->bool:
        p=self.root         #root노드부터 시작(물론 빈 트리라면 None이겠지만, add함수를 통해 값들이 삽입되었다고 가정)
        parent=None
        is_left_child=True

        while True:
            if p is None:
                return False
            if key==p.key:
                break
            else:
                p=parent
                if key<p.key:
                    is_left_child=True
                    p=p.left
                else:
                    is_left_child=False
                    p=p.right

        if p.left is None: #왼쪽자식이 없고
            if p is self.root:   #p 가 루트노드면
                self.root=p.right
            elif is_left_child: #p가 부모노드의 왼쪽자식이면,
                parent.left=p.right #부모노드의 왼쪽 포인터가 오른쪽자식을 가리킴
            else:
                parent.right=p.right

        if p.right is None: #오른쪽자식이 없고
            if p is self.root:   #p 가 루트노드면
                self.root=p.left
            elif is_left_child: #p가 부모노드의 왼쪽자식이면,
                parent.left=p.left #부모노드의 왼쪽 포인터가 오른쪽자식을 가리킴
            else:
                parent.right=p.left

        else: #자식이 2개임
            parent = p
            left=p.left
            is_left_child=True
            while left.right is not None: #우측 자식 노드가 없을 때가지
                parent=left
                left=left.right
                is_left_child=False

            p.key=left.key
            p.value=left.value
            if is_left_child:
                parent.left=left.left
            else:
                parent.right=left.left
        return True

    def dump(self)->None:

        def print_subtree(node:Node):
            if node is not None:
                print_subtree(node.left)
                print(f'{node.key}{node.value}')
                print_subtree(node.right)
        print_subtree(self.root)
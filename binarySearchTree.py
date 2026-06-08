class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root=None
    def insert(self,root,value):
        if root is None:
            return Node(value)
        if(value<root.value):
            root.left=self.insert(root.left,value)
        elif(value>root.value):
            root.right=self.insert(root.right,value)
        return root
    def search(self,root,key):
        if root is None:
            return False
        if root.value==key:
            return True
        if key<root.value:
            return self.search(root.left,key)
        return self.search(root.right,key)
    def min_value(self,root):
        current=root
        while current.left:
            current=current.left
        return current
    def max_value(self,root):
        current = root
        while current.right:
            current=current.right
        return current
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value, end=" ")
            self.inorder(root.right)
    def preorder(self, root):
        if root:
            print(root.value, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.value, end=" ")
    def delete_tree(self):
        self.root = None
        print("Tree deleted")

    def delete_node(self,root,value):
        if root is None:
            return None
        if root.value>value:
            root.right= self .insert

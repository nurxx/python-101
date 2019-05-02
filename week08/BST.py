class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,val):
        if self.data is not None:
            if val < self.data:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            elif val >= self.data:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
        else:
            self.data = val

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.data, end = ' || ')
        if self.right is not None:
            self.right.inorder()

    def preorder(self):
        print(self.data,end = ' || ')
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        print(self.data,end= ' || ')

if __name__ == '__main__':
    tree_root = Node()
    values = [4,4,7,8,122,11,9,3,6,65,55,71,98]
    for elem in values:
        tree_root.insert(elem)

    tree_root.inorder()
    print()
    tree_root.preorder()
    print()
    tree_root.postorder()
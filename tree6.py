class Node:

    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

    def insert(self,value):
        '''Insert method in binary tree:'''
        if self.value>value:
            if self.left:
                self.left.insert(value)
            else:
                self.left=Node(value)
        if self.value<value:
            if self.right:
                self.right.insert(value)
            else:
                self.right=Node(value)
        else:
            print("Duplication not allowed:")

    def preorder(self):

        '''Preorder traversal using morris method:'''

        root=self
        while root:
            if not root.left:
                print(root.value)
                root=root.right
            else:
                temp=root.left
                while temp.right!=root and temp.right!=None:
                    temp=temp.right
                if temp.right==None:
                    temp.right=root
                    print(root.value)
                    root=root.left
                else:
                    temp.right=None
                    root=root.right
                

    def inorder(self):

        '''Inorder traversal using morris method:'''

        root=self
        while root:
            if not root.left:
                print(root.value)
                root=root.right
            else:
                temp=root.left
                while temp.right!=root and temp.right!=None:
                    temp=temp.right
                if temp.right==None:
                    temp.right=root
                    root=root.left
                else:
                    temp.right=None
                    print(root.value)
                    root=root.right

if __name__=="__main__":
    print("=================================")
    print("Inorder morris traversal:")
    node=Node(12)
    node.insert(6)
    node.insert(4)
    node.insert(10)
    node.insert(2)
    node.insert(5)
    node.insert(24)
    node.insert(15)
    node.insert(32)
    node.insert(28)
    node.insert(36)
    print("===================================")
    print("Inorder traversal of the tree is:")
    node.inorder()
    print("====================================")
    print("The preorder traversal of the tree is:")
    node.preorder()
    print("==========================================")


